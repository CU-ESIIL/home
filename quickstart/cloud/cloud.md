---
title: Introduction to the Cloud Triangle
tags: [quickstart, cloud]
date: 2024-01-01
weight: 0.5
---

# Chapter: Working the CyVerse Cloud Triangle

<div style="padding:18px;border:1px solid #e5e7eb;border-radius:14px;background:linear-gradient(180deg,#f8fafc,#ffffff);margin:0 0 18px 0">
  <strong>What you’ll learn.</strong> Launch a CyVerse Discovery Environment (DE) instance, work entirely in the JupyterLab UI (no Git CLI), connect to GitHub over SSH using the Git sidebar widget, move data to and from the CyVerse Data Store with <em>GoCommands</em>, and—most importantly—ensure your work survives the end of an ephemeral compute session.
</div>

---

## 1. The Big Picture

Every project in this course lives on a triangle of services: <strong>compute</strong> on a DE instance, <strong>persistence</strong> in the CyVerse <strong>Data Store</strong>, and <strong>collaboration</strong> in <strong>GitHub (SSH)</strong>. Think of the instance as a bright, clean workbench: perfect for building, terrible for storage. When the lights turn off, anything left on the bench is gone. The Data Store is your long‑term memory. GitHub is your lab notebook—versioned, shareable, and accountable.

<div style="text-align:center;margin:18px 0">
<pre style="display:inline-block;text-align:left;padding:16px 18px;border:1px solid #e5e7eb;border-radius:12px;background:#fcfcfd">
        GitHub (SSH)
            ▲
            │  code · docs · small data (<100 MB)
            │
DE Instance ├──────────────▶ Data Store (CyVerse)
  (compute)                   (persistent files via <em>i:</em> paths)
</pre>
<em>Figure 1. The cloud triangle: where things live and how they move.</em>
</div>

> <strong>Golden Rule</strong>
> Never let the only copy of anything live on the DE instance.

<div style="padding:14px 16px;border:1px solid #e5e7eb;border-radius:12px;background:#eef2ff;margin:14px 0"><strong>Platform facts.</strong> The Discovery Environment’s interactive apps are called <em>VICE</em>. JupyterLab‑based images include a Git sidebar widget so you can clone, pull, stage, commit, and push without a shell. The Data Store is iRODS‑backed and exposed at <code>/iplant/home/&lt;username&gt;</code>. <strong>GoCommands addresses the Data Store using the <code>i:</code> scheme</strong>, e.g., <code>i:/iplant/home/&lt;username&gt;/…</code>. A WebDAV endpoint exists at <code>https://data.cyverse.org/dav/iplant/home/&lt;username&gt;</code> for small transfers; use GoCommands for large or bulk data.</div>

---

## 2. Key Ideas (told as a story)

You begin at the instance—a virtual machine launched in the Discovery Environment. Its software comes pre‑packed in a container image so collaborators start from the same tools. Inside JupyterLab, you open the left‑hand <em>Git</em> sidebar. That widget becomes your control center for the repository: you paste an SSH clone URL, watch files appear, stage changes with checkboxes, write a commit message, and press <em>Push</em> when you’re satisfied.

Your code arrives quickly. Your data is heavier. For that you turn to the Data Store. Using <strong>GoCommands</strong>—a resilient, resumable transfer tool—you pull only what you need into a local <code>data/</code> folder for this run using <strong><code>i:</code> paths</strong>. You compute on the instance as if it were a scratch pad: fast, flexible, and temporary. When you finish, you push code and notes back to GitHub through the widget and send large outputs home to the Data Store. Only after both are safe do you shut the instance down.

<div style="padding:12px 14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc;margin-top:10px"><strong>Reality check.</strong> The DE file browser is handy for tiny files. Browser uploads work best below about <em>2&nbsp;GB per file</em>. WebDAV is fine for small/medium transfers but is not recommended for very large files (≈10+ GiB). Use GoCommands for anything large or important.</div>

---

## 3. Definitions (boxed for quick reference)

<div style="display:grid;gap:12px">
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>Instance.</strong> A running virtual computer in CyVerse DE. Ephemeral—files vanish when it stops. Interactive apps are called <em>VICE</em>.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>Container / Image.</strong> The prebuilt software environment that makes runs reproducible across machines.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>JupyterLab Git widget.</strong> The left‑sidebar panel in DE’s JupyterLab that lets you <em>clone</em>, <em>pull</em>, <em>stage</em>, <em>commit</em>, and <em>push</em> without using the CLI. It also shows history, branches, and notebook‑aware diffs.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>SSH key.</strong> A cryptographic keypair that lets the instance authenticate to GitHub without passwords (works cleanly with 2FA). Once configured, the Git widget uses it transparently.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>Data Store path.</strong> Your home is <code>/iplant/home/&lt;username&gt;</code>. <em>When using GoCommands, prefix with <code>i:</code></em>, e.g., <code>i:/iplant/home/&lt;username&gt;/projects/…</code>.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>GoCommands (<code>gocmd</code>).</strong> A cross‑platform CLI for iRODS/Data Store. We install it in‑instance, initialize it with <code>./gocmd init</code>, and use flags like <code>--diff</code>, <code>--icat</code>, <code>--retry</code>, <code>-d</code>, and <code>-k</code> for robust, checksum‑verified transfers.</div>
  <div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc"><strong>Ephemeral vs. Persistent.</strong> Ephemeral disappears when compute stops; persistent remains until you delete it. The Data Store is the canonical home for datasets and large outputs.</div>
</div>

---

## 4. Your First Loop (start → finish without losing anything)

<strong>Launch</strong> a DE instance with the JupyterLab‑based image your course specifies, then open JupyterLab.

<div style="padding:14px 16px;border:1px solid #e5e7eb;border-radius:12px;background:#fff7ed;margin:14px 0"><strong>One‑time SSH setup for the Git widget.</strong> If your image doesn’t preinstall a key, generate one in a tiny terminal step, add it to GitHub, and you’re done:

<code>ssh-keygen -t ed25519 -C "you@org.edu" -f ~~/.ssh/id_ed25519</code><br/>
<code>eval "$(ssh-agent -s)" &amp;&amp; ssh-add ~~/.ssh/id_ed25519</code><br/>
Copy <code>~~/.ssh/id_ed25519.pub</code> into GitHub → Settings → SSH keys. The widget will now use SSH transparently. <br/><em>Security note:</em> your private key stays in the instance; treat <code>~~/.ssh/id_ed25519</code> as sensitive even though instances are ephemeral.
</div>

<div style="padding:12px 14px;border:1px solid #e5e7eb;border-radius:12px;background:#fff7ed;margin:10px 0"><strong>Path note.</strong> Use <code>~/.ssh/…</code> (tilde means “your home directory,” e.g., <code>/home/jovyan</code>). A leading <code>/</code> points to the filesystem root, so <code>/.ssh/…</code> is wrong in user space. Also ensure permissions are correct:

<code>mkdir -p ~/.ssh &amp;&amp; chmod 700 ~/.ssh</code><br/>
<code>chmod 600 ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub</code>
</div>

<strong>Clone with the Git widget.</strong> Open the left sidebar → <em>Git</em> (branch icon) → <em>Clone a Repository</em>. Paste the SSH URL, e.g. <code>git@github.com:ORG/REPO.git</code>. Choose a local folder (e.g., <code>/home/jovyan/</code>). When the clone finishes, click <em>Change Directory</em> to open the repo.

<strong>Pull/Stage/Commit/Push—still in the widget.</strong> Use the file‑level checkboxes to stage changes, type a message in the commit box, click <em>Commit</em>, then click <em>Push</em>. Use <em>Pull</em> to sync before you start the day or when collaborators push changes.

<div style="padding:16px;border:1px solid #e5e7eb;border-radius:12px;background:#ecfdf5;margin:18px 0"><strong>Install GoCommands in the instance (one‑liner).</strong><br/>
<code>GOCMD_VER=$(curl -L -s https://raw.githubusercontent.com/cyverse/gocommands/main/VERSION.txt); \</code><br/>
<code>curl -L -s https://github.com/cyverse/gocommands/releases/download/${GOCMD_VER}/gocmd-${GOCMD_VER}-linux-amd64.tar.gz | tar zxvf -</code>

Now initialize and verify access:<br/>
<code>./gocmd init</code><br/>
<code>./gocmd whoami</code><br/>
<em>Note:</em> the binary is in the current directory; move it to <code>~/bin/</code> and add that to your <code>PATH</code> to run it as <code>gocmd</code> without the leading <code>./</code>.
</div>

<strong>Fetch data</strong> from the Data Store using <strong><code>i:</code> paths</strong>. Pull into <code>data/</code>:

```bash
mkdir -p data
./gocmd get --icat --retry 3 -d -k -r \
  i:/iplant/home/<your-username>/projects/myproj/data/ \
  ./data/
```

<strong>Work</strong> in notebooks and scripts. Keep big intermediates in a timestamped folder, e.g. <code>outputs/run-YYYYMMDD/</code>. When finished, save work in the right places. A typical, robust upload looks like this:

```bash
./gocmd put --diff --icat --retry 3 -d -k \
  cross-sensor-cal/table_mountain \
  i:/iplant/home/shared/earthlab/macrosystems/processed_flight_lines/table_mountain_calibration_flightline \
  > debug_log.txt 2>&1
```

Only then do you <strong>shut the instance down</strong>. Your results now live safely in GitHub and the Data Store.

---

## 5. A Project That Teaches Good Habits

Organize your repository so newcomers can rerun it without guessing.

```
repo/
  README.md
  docs/                  # publish via GitHub Pages
  env/                   # environment.yml or requirements.txt; record the image tag
  src/                   # source code
  notebooks/             # keep light; no giant outputs
  configs/               # YAML/JSON parameters used for runs
  scripts/               # fetch_data.sh, push_outputs.sh
  data/                  # tiny samples only; real data lives in Data Store
    README.md            # where to get real data with gocmd
  outputs/               # tiny examples only; big outputs go to Data Store
```

In <code>data/README.md</code>, give learners a single command to fetch the real data (note the <code>i:</code> prefix):

```md
Large datasets live in the CyVerse Data Store:
i:/iplant/home/<you>/projects/myproj/data/

Fetch them into this folder with:
./gocmd get --icat --retry 3 -d -k -r i:/iplant/home/<you>/projects/myproj/data/ ./data/
```

Provide helper scripts so no one memorizes paths:

```bash
# scripts/fetch_data.sh
#!/usr/bin/env bash
set -euo pipefail
REMOTE="i:/iplant/home/<you>/projects/myproj/data/"
LOCAL="./data"
mkdir -p "$LOCAL"
./gocmd get --icat --retry 3 -d -k -r "$REMOTE" "$LOCAL/"
```

```bash
# scripts/push_outputs.sh
#!/usr/bin/env bash
set -euo pipefail
REMOTE="i:/iplant/home/<you>/projects/myproj/outputs/"
LOCAL="./outputs"
[[ -d "$LOCAL" ]] || { echo "No outputs/ to push"; exit 0; }
./gocmd put --diff --icat --retry 3 -d -k "$LOCAL/" "$REMOTE"
```

Make both executable with <code>chmod +x scripts/*.sh</code>.

---

## 6. Before You Power Down (a single card to read)

<div style="padding:16px;border:1px solid #e5e7eb;border-radius:12px;background:#f1f5f9">
<strong>Pre‑shutdown checklist</strong>

- The Git sidebar shows no unstaged changes; last commit is pushed (SSH).  
- Large outputs are in the Data Store via <code>./gocmd put --diff --icat --retry 3 -d -k</code>.  
- (Optional) Checksums verified for critical files and confirm <code>debug_log.txt</code> shows no failed transfers.  
- The container image tag and run config are recorded under <code>env/</code> or <code>configs/</code>.
</div>

---

## 7. Troubleshooting by Symptom (quick reads)

<div style="padding:14px;border:1px solid #fee2e2;border-radius:12px;background:#fef2f2;margin-bottom:12px">
<strong>Lost files after shutdown.</strong> They only lived on the instance. Always push via the Git widget and/or <code>./gocmd put</code> to the Data Store before stopping compute.
</div>

<div style="padding:14px;border:1px solid #e0e7ff;border-radius:12px;background:#eef2ff;margin-bottom:12px">
<strong>“Push failed / authentication required.”</strong> Your remote is HTTPS. In the Git widget, open <em>Repository → Remote</em> and set the URL to the SSH form, e.g., <code>git@github.com:ORG/REPO.git</code>. Ensure your SSH key is added to GitHub.
</div>

<div style="padding:14px;border:1px solid #d1fae5;border-radius:12px;background:#ecfdf5;margin-bottom:12px">
<strong>GoCommands can’t see storage.</strong> Re‑initialize (<code>./gocmd init</code>), confirm <code>./gocmd whoami</code>, and verify the <code>i:/iplant/home/&lt;username&gt;/…</code> path spelling.
</div>

<div style="padding:14px;border:1px solid #fde68a;border-radius:12px;background:#fffbeb;margin-bottom:12px">
<strong>“.h5 file signature not found.”</strong> You saved an HTML error as <code>.h5</code>. Validate type with <code>file</code> and the first bytes (<code>89 48 44 46 0d 0a 1a 0a</code>). Re‑download from the Data Store with <code>./gocmd get --icat --retry 3 -d -k</code> and an <code>i:</code> path.
</div>

<div style="padding:14px;border:1px solid #e5e7eb;border-radius:12px;background:#f8fafc">
<strong>Slow or stalling transfers in the browser.</strong> The DE file browser handles one file at a time and works best under ~2&nbsp;GB. For larger files or many files, switch to GoCommands. WebDAV is okay for smaller files via <code>https://data.cyverse.org/dav</code>, but avoid it for very large files.
</div>

---

## 8. Why This Works (short reflection)

Separating compute from storage and collaboration is not bureaucracy—it’s robustness. The JupyterLab Git widget lowers the barrier to good Git hygiene. Containers make your environment predictable. GitHub gives your ideas a history. The Data Store protects your heavy, precious artifacts. The triangle is a habit; once it clicks, every project becomes easier to explain, repeat, and trust.

---

## 9. Self‑Check (two minutes)

1) What survives when the instance stops?  
2) Which tool should you use for a 20&nbsp;GB transfer and why?  
3) Why do we insist on SSH for GitHub even when using the widget?  
4) Where does the canonical copy of your dataset live?

<details>
<summary><em>Suggested answers</em></summary>
Ephemeral compute does not; only what you pushed to GitHub and stored in the Data Store. Use GoCommands for reliable, resumable large transfers with <code>i:</code> paths. SSH avoids passwords and works cleanly with 2FA and the Git widget. The canonical dataset lives in the Data Store.
</details>

---

## Appendix A: The JupyterLab Git Widget — Deep Dive

<div style="padding:16px;border:1px solid #e5e7eb;border-radius:12px;background:linear-gradient(180deg,#f8fafc,#ffffff);margin:0 0 14px 0">
  <strong>What it is.</strong> The Git widget is JupyterLab’s built‑in panel for Git operations. It lets you clone, view status, stage files, write a commit message, push/pull to remotes, browse history, switch/create branches, and open diffs — all without leaving the notebook UI.
</div>

### The panel at a glance
Open the <em>Git</em> icon in the left sidebar. The top toolbar shows actions (Clone, Pull, Push, Branches, History). The main list reflects your working tree: changed files, staged files, and untracked files. Clicking a file can open a rich diff; double‑click can be set to open diffs by default in <em>Settings → Advanced Settings → Git</em> (see <code>doubleClickDiff</code>).

<div style="padding:12px 14px;border:1px solid #e5e7eb;border-radius:12px;background:#ecfdf5;margin:12px 0"><strong>Notebook‑aware diffs.</strong> When you diff a <code>.ipynb</code>, the widget renders a cell‑by‑cell view rather than raw JSON, making changes readable for reviewers.
</div>

### First‑time setup (once per image)
Generate an SSH key, add it to the agent, and paste the public key into your GitHub account. After that, the widget can authenticate seamlessly over SSH for clone/pull/push.

```bash
ssh-keygen -t ed25519 -C "you@org.edu" -f ~~/.ssh/id_ed25519
eval "$(ssh-agent -s)" && ssh-add ~~/.ssh/id_ed25519
cat ~~/.ssh/id_ed25519.pub   # copy into GitHub → Settings → SSH keys
```

Use the SSH URL (e.g., <code>git@github.com:ORG/REPO.git</code>) for <em>Clone a Repository</em>.

### Daily flow inside the widget
Pull, edit, stage, commit, push. Use History to review changes; Branches to isolate work.

### Quick troubleshooting
<div style="display:grid;gap:10px">
  <div style="padding:12px;border:1px solid #fee2e2;border-radius:12px;background:#fef2f2"><strong>“The Git panel is missing.”</strong> Launch an image that bundles the extension, or enable it if your image supports extensions.</div>
  <div style="padding:12px;border:1px solid #e0e7ff;border-radius:12px;background:#eef2ff"><strong>“Push/clone fails with 500 errors.”</strong> Configure credentials. Prefer SSH; if you must use HTTPS, the widget can temporarily cache credentials.</div>
  <div style="padding:12px;border:1px solid #d1fae5;border-radius:12px;background:#ecfdf5"><strong>“The panel doesn’t see my repo.”</strong> Make sure the file browser is focused on a folder that contains a <code>.git/</code> directory.</div>
</div>



