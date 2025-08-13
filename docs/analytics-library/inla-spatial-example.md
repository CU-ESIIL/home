---
title: Spatial modeling in R with INLA
myst:
  html_meta:
    description: 'Spatial Bayesian analysis using the INLA package in R with a BYM model on areal data.'
tags: [analytics, r, inla, spatial]
---

# Spatial Modeling with INLA in R

The Integrated Nested Laplace Approximation (INLA) package enables fast Bayesian inference for latent Gaussian models. This example follows the INLA documentation to fit a spatial Besag-York-Mollié (BYM) model to North Carolina sudden infant death syndrome (SIDS) counts.

## Prerequisites

- [R](https://www.r-project.org)
- [INLA](https://www.r-inla.org) package
- [`spdep`](https://CRAN.R-project.org/package=spdep), [`spData`](https://CRAN.R-project.org/package=spData), and [`sf`](https://CRAN.R-project.org/package=sf) packages for spatial data handling

```r
# install INLA from the project repository if needed
if (!require(INLA)) {
  install.packages("INLA", repos = "https://inla.r-inla-download.org/R/stable")
  library(INLA)
}
```

## Load data and build adjacency

```r
library(spdep)
library(spData)
library(sf)

# county polygons and SIDS data
nc <- st_read(system.file("shapes/nc.shp", package = "spData"), quiet = TRUE)

# neighborhood structure and graph for INLA
nb <- poly2nb(nc)
INLA::nb2INLA("nc.adj", nb)   # writes adjacency file
g <- INLA::inla.read.graph("nc.adj")

nc$ID <- 1:nrow(nc)  # unique identifier for spatial random effect
```

## Fit a spatial BYM model

The response is the 1974 SIDS counts (`SID74`) with births (`BIR74`) as the expected number of cases.

```r
formula <- SID74 ~ 1 + f(ID, model = "bym", graph = g)
result <- inla(
  formula,
  family = "poisson",
  data = nc,
  E = BIR74,
  control.predictor = list(compute = TRUE)
)

summary(result)
```

## Map fitted risks

```r
nc$fitted <- result$summary.fitted.values[, "mean"]
plot(nc["fitted"], main = "Estimated SIDS risk")
```

This workflow demonstrates how INLA can be applied to spatial data for disease mapping or other areal analyses.

