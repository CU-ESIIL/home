---
title: Working the Cloud Triangle
tags: [quickstart, cloud, cyverse]
date: 2024-01-01
---

# Chapter: Working the CyVerse Cloud Triangle

> **What you’ll learn**
> Launch a CyVerse Discovery Environment (DE) JupyterLab session, connect to GitHub with SSH through the Git sidebar, move data with GoCommands, and—most importantly—keep your work alive after an ephemeral compute session ends.

---

## 1. Why the Triangle?

Across science platforms like **BinderHub**, **JupyterHub classrooms**, and cloud services such as **Azure ML** or **Vertex AI Workbench**, the same pattern repeats:

1. **GitHub** (or GitLab, etc.) for *code & collaboration*  
2. **Ephemeral compute** (JupyterLab, containerized notebooks, VICE apps) for *analysis*  
3. **Persistent storage** (cloud volumes, object stores, CyVerse Data Store) for *datasets and results*

This is the **Cloud Triangle**. It’s not bureaucracy—it’s the habit that keeps your work reproducible, durable, and shareable.

Think of it like this:

- **Compute** = your scratch pad: fast but disposable  
- **GitHub** = your lab notebook: versioned, accountable, and collaborative  
- **Data Store** = your filing cabinet: heavy, permanent, and backed up

![Cloud Triangle Diagram](home/docs/assets/art_gallery/cloud_triangle_diagram.png)

> **Golden Rule**  
> Never let the only copy of your work live on the instance. If you don’t push to GitHub or save to the Data Store, it will vanish when compute stops.

---

## 2. The Journey (narrative)

1. **You begin at the instance.** You launch a JupyterLab session in the Discovery Environment. This containerized image ensures everyone starts with the same software.  
2. **You connect GitHub.** In the Git sidebar, you paste an SSH clone URL. Files appear instantly. With checkboxes you stage changes, commit, and push—no shell required.  
3. **You fetch data.** Code is light, data is heavy. For datasets, you use **GoCommands**, a resumable transfer tool. With the `i:` prefix, you pull just what you need into `./data/` for this run.  
4. **You compute.** The instance is your scratch pad. Notebooks run quickly, intermediate files pile up. But you remember: they’re temporary.  
5. **You preserve.** Finished code goes back to GitHub; large results go to the Data Store. Only then do you shut the instance down, confident that nothing important will be lost.  

This rhythm—**clone → compute → preserve**—is the triangle in motion. It’s the same rhythm used in BinderHub sessions, JupyterHub classrooms, and professional cloud notebooks worldwide.

---

## 3. Quick Definitions

- **Instance.** A temporary virtual machine running in CyVerse DE (aka a VICE app). Files vanish when it stops.
- **Container / Image.** The prebuilt software environment (JupyterLab, Python, R, etc.) that makes runs reproducible.
- **Git widget.** The JupyterLab sidebar that lets you clone, pull, commit, and push over SSH without a terminal.
- **SSH key.** A password-free credential that lets the instance authenticate to GitHub. Works cleanly with 2FA.
- **Data Store path.** Your home lives at `/iplant/home/<username>`. With GoCommands, prefix with `i:`, e.g. `i:/iplant/home/<username>/projects/...`.
- **GoCommands.** Cross-platform CLI for the Data Store. Robust, resumable, checksum-verified transfers.
- **Ephemeral vs Persistent.** Ephemeral = gone when compute stops. Persistent = survives (Data Store, GitHub).

---

## 4. Your First Loop (step-by-step)

1. **Launch an instance.** Choose the JupyterLab-based image your course specifies.  
2. **Set up SSH (one-time).**  
   ```bash
   ssh-keygen -t ed25519 -C "you@org.edu" -f ~/.ssh/id_ed25519
   eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
   cat ~/.ssh/id_ed25519.pub   # add to GitHub → Settings → SSH keys
   ```
   > Keys live in `~/.ssh/` (your home). Never use `/.ssh/` (the root).
3. **Clone with the Git widget.** Open the Git sidebar → “Clone a Repository” → paste `git@github.com:ORG/REPO.git`.  
4. **Commit & push.** Stage files with checkboxes, write a commit message, press **Commit**, then **Push**.  
5. **Install GoCommands.**  
   ```bash
   GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \
   curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -
   ./gocmd init
   ./gocmd whoami
   ```
6. **Fetch data.**  
   ```bash
   mkdir -p data
   ./gocmd get --icat --retry 3 -d -k -r \
     i:/iplant/home/<username>/projects/myproj/data/ \
     ./data/
   ```
7. **Push outputs back.**  
   ```bash
   ./gocmd put --diff --icat --retry 3 -d -k \
     outputs/run-20240101/ \
     i:/iplant/home/<username>/projects/myproj/outputs/
   ```
8. **Shut down safely.** Code is in GitHub, data is in the Data Store—nothing left behind.

---

## 5. Good Project Habits

Structure your repo so collaborators (and future-you) can rerun it without guessing:

```
repo/
  README.md
  env/              # environment.yml or requirements.txt
  src/              # source code
  notebooks/        # small notebooks only
  configs/          # YAML/JSON configs
  data/             # samples only; real data via Data Store
    README.md       # points to i: paths
  outputs/          # tiny examples; real outputs in Data Store
  scripts/          # fetch_data.sh, push_outputs.sh
```

In `data/README.md`, include a one-liner to fetch real data:

```md
Fetch real data with:
./gocmd get --icat --retry 3 -d -k -r i:/iplant/home/<username>/projects/myproj/data/ ./data/
```

---

## 6. Before You Power Down (checklist)

- Git sidebar shows no unstaged changes; last commit pushed.  
- Outputs uploaded with `./gocmd put`.  
- Critical files verified (checksums / `debug_log.txt`).  
- Container image tag and configs recorded in `env/` or `configs/`.

---

## 7. Troubleshooting (by symptom)

- **Lost files after shutdown** → They only lived on the instance. Always push to GitHub or the Data Store.  
- **Push failed / needs password** → Remote is HTTPS. Switch to SSH (`git@github.com:ORG/REPO.git`) and add your SSH key to GitHub.  
- **GoCommands can’t see storage** → Rerun `./gocmd init`, confirm `./gocmd whoami`, check `i:/iplant/home/<username>/…`.  
- **“.h5 signature not found”** → You saved an error page as `.h5`. Re-download with `./gocmd get`.  
- **Slow browser uploads** → Browser best under 2 GB. Use GoCommands for large files.

---

## 8. Why This Works

BinderHub sessions, JupyterHub classrooms, and cloud notebooks all follow the same pattern:

- ephemeral compute  
- Git-backed collaboration  
- persistent storage

By adopting this rhythm in CyVerse, you ensure your work is robust, repeatable, and explainable. Once the triangle clicks, every project is easier to trust and share.

---

## 9. Self-Check (2 minutes)

1. What survives when the instance stops?  
2. Which tool do you use for a 20 GB transfer?  
3. Why SSH for GitHub instead of HTTPS?  
4. Where does the canonical copy of your dataset live?

<details>
<summary>Answers</summary>

1. Only what you pushed to GitHub or saved in the Data Store.  
2. GoCommands (resumable, checksum-verified, `i:` paths).  
3. SSH avoids passwords, works with 2FA, integrates with the Git widget.  
4. In the Data Store, not on the instance.

</details>

