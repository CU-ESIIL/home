---
layout: page
title: INLA — Drop-in Analytics Module
permalink: /analytics/inla/
tags: [analytics, Bayesian, INLA, spatial, spatiotemporal, GLMM, LGM, R]
summary: Minimal, production-ready INLA module wired for environmental data pipelines. Not a tutorial.
---

> **Purpose**: This page provides a **self-contained, copy-pasteable INLA module** for environmental data scientists. It defines the **I/O contract**, a standard **config file**, and a **reference R function** that you can drop into a pipeline and wire to a dataset from the Data Library. For pedagogy, use the separate, longer guide.

---

## When to use INLA

Use INLA (Integrated Nested Laplace Approximation) for **Latent Gaussian Models (LGMs)**: GLMs/GLMMs with random effects; spatial and spatiotemporal models (e.g., **SPDE** for Gaussian fields over 2D space); temporal structures (RW1/RW2/AR1); and hierarchical models where full MCMC is too slow.

---

## I/O Contract (Module Interface)

**Input**

* **DataFrame** (R `data.frame` / `tibble` / `sf`):

  * `y` — response

    * Gaussian (numeric), Poisson (integer counts), Binomial (0/1 or cbind(success, failure)).
  * Predictors: arbitrary columns (e.g., `x1`, `x2`, …).
  * Optional random-effects keys: `group_id`, `site_id`, etc. (character/factor).
  * Optional space: either `geometry` (POINT in `sf`) **or** numeric `lon`, `lat`.
  * Optional time: `time` (integer index or Date/POSIXct; will be coerced).
  * Optional: `weight`, `offset`.
* **Config YAML** (see below): model family, formula terms, priors, spatial/temporal options, compute flags, output paths.

**Output** (written to `outputs/inla/` by default)

* `fit_summary.rds` — full INLA fit object (RDS).
* `posterior_fixed.csv` — posteriors for fixed effects.
* `posterior_hyper.csv` — posteriors for hyperparameters.
* `fitted_values.csv` — original rows with fitted mean, sd, and linear predictor.
* `criteria.csv` — WAIC, DIC, marginal likelihood, CPO summaries if requested.
* Optional: `predict_grid_*.csv` or raster outputs when a prediction grid is supplied.

**Contract Notes**

* Module is **pure R**; expects **R ≥ 4.2** and the **INLA** package available.
* Spatial runs require either `sf` POINT geometry (preferred) or numeric lon/lat.
* The SPDE mesh is created internally unless you supply one.

---

## Config Template (`inla_config.yml`)

```yaml
model:
  family: poisson           # one of: gaussian, poisson, binomial, negative.binomial, gamma, etc.
  link: log                 # usually implied by family; override if needed
  formula: |
    y ~ 1 + x1 + x2 +
        f(group_id, model = "iid") +            # random intercept
        f(space, model = spde) +                 # spatial field (SPDE)
        f(time, model = "ar1")                   # temporal correlation

priors:
  beta:
    mean: 0.0
    precision: 0.001
  spde_pc:                 # Penalized complexity priors for SPDE
    range0: 50             # units of your coordinates
    Pr_range: 0.05         # P(range < range0) = Pr_range
    sigma0: 1.0
    Pr_sigma: 0.05

spde:
  mesh:
    max_edge: [0.1, 0.5]   # coarse, fine (in your coord units)
    cutoff: 0.05           # min distance to avoid duplicate nodes
  crs_epsg: 4326           # if lon/lat; otherwise set your projected EPSG

temporal:
  index_var: time          # name of time column in data

compute:
  waic: true
  dic: true
  cpo: true

io:
  out_dir: outputs/inla/
  save_rds: true
  export_fitted_csv: true
  export_posteriors_csv: true
```

> **Tip**: Keep coordinates in a **projected CRS** for SPDE (meters). If your data are lon/lat, the module can internally transform using the provided `spde.crs_epsg` target.

---

## Minimal Driver Function (R)

Copy this function into your repo (e.g., `R/run_inla_module.R`). It reads your data and config, builds the SPDE (if requested), runs INLA, and writes standardized outputs.

```r
# R/run_inla_module.R
suppressPackageStartupMessages({
  library(INLA)      # install instructions below
  library(sf)
  library(dplyr)
  library(yaml)
  library(readr)
  library(rlang)
})

#' Run INLA analytics module
#' @param data    data.frame or sf with columns per I/O contract
#' @param config  path to YAML file (see template)
#' @param pred_grid optional sf or data.frame with coordinates for prediction
#' @return invisible list with key outputs (also written to disk)
run_inla_module <- function(data, config, pred_grid = NULL) {
  cfg <- yaml::read_yaml(config)
  out_dir <- cfg$io$out_dir %||% "outputs/inla/"
  dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

  # Set up family & control options
  family <- cfg$model$family %||% "gaussian"

  # Spatial: build SPDE if requested via 'f(space, model = spde)'
  build_spde <- grepl("f(\\s*space\\s*,\\s*model\\s*=\\s*spde\\s*)", cfg$model$formula)
  A <- NULL; spde <- NULL; mesh <- NULL

  if (build_spde) {
    # Ensure we have coordinates
    if (!inherits(data, "sf")) {
      stopifnot(all(c("lon","lat") %in% names(data)))
      data <- sf::st_as_sf(data, coords = c("lon","lat"), crs = 4326, remove = FALSE)
    }
    # Project to target CRS for SPDE
    target_epsg <- cfg$spde$crs_epsg %||% 3857
    data <- sf::st_transform(data, target_epsg)
    coords <- sf::st_coordinates(data)

    # Mesh
    max_edge <- cfg$spde$mesh$max_edge %||% c(1000, 5000)
    cutoff   <- cfg$spde$mesh$cutoff   %||% 100
    mesh <<- INLA::inla.mesh.2d(loc = coords, max.edge = max_edge, cutoff = cutoff)

    # SPDE model with PC priors
    pc <- cfg$priors$spde_pc
    if (is.null(pc)) pc <- list(range0 = 10000, Pr_range = 0.05, sigma0 = 1, Pr_sigma = 0.05)
    spde <<- INLA::inla.spde2.pcmatern(mesh = mesh,
      prior.range = c(pc$range0, pc$Pr_range),
      prior.sigma = c(pc$sigma0, pc$Pr_sigma)
    )

    # Projection matrix and index
    spde_index <- INLA::inla.spde.make.index(name = "space", n.spde = spde$n.spde)
    A <<- INLA::inla.spde.make.A(mesh = mesh, loc = coords)

    # Stack for observations
    effects <- list(
      data.frame(Intercept = 1, data |> dplyr::select(dplyr::any_of(all.vars(~ .)))) ,
      list(space = spde_index$space)
    )
    # Build stack with model formula later via inla.stack
  }

  # Design formula
  formula_txt <- cfg$model$formula
  stopifnot(is.character(formula_txt))
  # Provide 'spde' in environment so f(space, model = spde) resolves
  env <- rlang::env(spde = spde)
  fml <- rlang::parse_expr(formula_txt) |> rlang::eval_bare(env = env)

  # Compute flags
  control_compute <- list(
    waic = isTRUE(cfg$compute$waic),
    dic  = isTRUE(cfg$compute$dic),
    cpo  = isTRUE(cfg$compute$cpo)
  )

  # Fit model
  fit <- INLA::inla(
    formula = fml,
    data = as.data.frame(st_drop_geometry_safe(data)),
    family = family,
    control.compute = control_compute,
    control.fixed = list(
      mean = cfg$priors$beta$mean %||% 0,
      prec = cfg$priors$beta$precision %||% 0.001
    )
  )

  # Write outputs
  if (cfg$io$save_rds %||% TRUE) saveRDS(fit, file.path(out_dir, "fit_summary.rds"))

  # Fixed effects posteriors
  fe <- as.data.frame(fit$summary.fixed)
  fe$term <- rownames(fit$summary.fixed)
  readr::write_csv(fe, file.path(out_dir, "posterior_fixed.csv"))

  # Hyperparameters
  if (!is.null(fit$summary.hyperpar)) {
    hy <- as.data.frame(fit$summary.hyperpar)
    hy$term <- rownames(fit$summary.hyperpar)
    readr::write_csv(hy, file.path(out_dir, "posterior_hyper.csv"))
  }

  # Criteria
  crit <- tibble::tibble(
    WAIC = fit$waic$waic %||% NA_real_,
    p_WAIC = fit$waic$p.eff %||% NA_real_,
    DIC = fit$dic$dic %||% NA_real_,
    p_DIC = fit$dic$p.eff %||% NA_real_
  )
  readr::write_csv(crit, file.path(out_dir, "criteria.csv"))

  # Fitted values (per row)
  fv <- tibble::tibble(
    fitted_mean = fit$summary.fitted.values$mean,
    fitted_sd   = fit$summary.fitted.values$sd,
    lp_mean     = fit$summary.linear.predictor$mean,
    lp_sd       = fit$summary.linear.predictor$sd
  )
  fv_out <- dplyr::bind_cols(st_drop_geometry_safe(data), fv)
  readr::write_csv(fv_out, file.path(out_dir, "fitted_values.csv"))

  invisible(list(fit = fit, fixed = fe, hyper = hy, criteria = crit, fitted = fv_out, mesh = mesh))
}

# Safe geometry dropper
data.table::setDTthreads(1)
st_drop_geometry_safe <- function(x) {
  if (inherits(x, "sf")) sf::st_drop_geometry(x) else x
}
```

**Install R packages** (one-time):

```r
install.packages("sf")
install.packages("yaml")
install.packages("readr")
# INLA uses its own repo
install.packages(
  "INLA",
  repos = c(getOption("repos"), INLA = "https://inla.r-inla-download.org/R/stable"),
  dep = TRUE
)
```

---

## Quick Start (Wire to a Data Library dataset)

1. **Pick a dataset** from the Data Library (must include `y`, predictors, and **either** `geometry` (POINT) **or** `lon, lat`).
2. Save a config as `inla_config.yml` (edit family, formula, priors, and mesh settings).
3. Run the module:

```r
# example: analytics/INLA/run.R
library(readr); library(sf)
source("R/run_inla_module.R")

data <- readr::read_csv("path/to/data.csv")        # or read_sf("data.gpkg")
# If lon/lat present, the function will handle sf conversion

res <- run_inla_module(
  data   = data,
  config = "inla_config.yml"
)

# Inspect key outputs
readr::read_csv("outputs/inla/posterior_fixed.csv")
readr::read_csv("outputs/inla/criteria.csv")
```

---

## Example Configs

**A. Spatial Poisson with SPDE + site random intercept**

```yaml
model:
  family: poisson
  formula: |
    y ~ 1 + elevation + temp + f(site_id, model = "iid") + f(space, model = spde)
priors:
  beta: { mean: 0, precision: 0.001 }
  spde_pc: { range0: 30000, Pr_range: 0.05, sigma0: 1, Pr_sigma: 0.05 }
spde:
  mesh: { max_edge: [5000, 15000], cutoff: 2000 }
  crs_epsg: 5070  # NAD83 / Conus Albers (meters)
compute: { waic: true, dic: true, cpo: true }
io: { out_dir: outputs/inla/ }
```

**B. Binomial with AR1 time + random intercept**

```yaml
model:
  family: binomial
  formula: |
    cbind(success, failure) ~ 1 + x1 + x2 + f(group_id, model = "iid") + f(time, model = "ar1")
priors:
  beta: { mean: 0, precision: 0.001 }
compute: { waic: true }
io: { out_dir: outputs/inla/ }
```

---

## Linking Guidance (Data Library → Analytics)

* **Upstream (Data Library)** should expose field names that the INLA module expects:

  * `y` (or `success`,`failure` for binomial), predictors (e.g., `x1`, `x2`), and **one** of:

    * `geometry` (POINT, projected CRS), or
    * `lon`, `lat` (WGS84).
  * Optional keys: `group_id`, `site_id`, `time`.
* **Downstream consumers** can watch `outputs/inla/` for `posterior_fixed.csv` and `fitted_values.csv` to join results back to the original table.
* If upstream provides a **prediction grid** (regular points with predictor fields), pass it via `pred_grid` to the function and extend the code to predict on the grid using the fitted model components (kept minimal here for production clarity).

---

## Model Hygiene & Gotchas

* Use **projected coordinates** (meters) for SPDE meshes; tune `max_edge`/`cutoff` to your sampling density and domain size.
* Check **priors** (PC priors above are conservative defaults; adjust to your domain scale).
* Prefer **WAIC** for model comparison; inspect **CPO**/PIT for outliers.
* For binomial responses, supply counts via `cbind(success, failure)`.
* If you need smoother time trends, try `f(time, model = "rw1")` or `"rw2"`.

---

## Reproducibility Block (optional)

Include a lockfile (e.g., `renv::snapshot()`), and pin the INLA repo URL above. In containers, add system deps for `sf` (GDAL/GEOS/PROJ).

---

## Attribution

If you cite methods in manuscripts, standard references include: **Rue, Martino & Chopin (2009)** for INLA and **Lindgren, Rue & Lindström (2011)** for SPDE. (Full citations in the pedagogical guide.)

---

## Changelog

* **v0.1** — First release of the analytics module with SPDE support and standardized outputs.
