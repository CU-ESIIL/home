---
title: Introduction to the Cloud Triangle
tags: [quickstart, cloud]
date: 2024-01-01
weight: 0.5
---

# Introduction to the Cloud Triangle

![Diagram of the cloud triangle showing connections among GitHub, a cloud instance, and persistent storage](cloud-triangle.svg)

The cloud triangle illustrates how work moves among three services: a cloud compute instance, persistent storage, and GitHub. Each side of the triangle represents a connection, and understanding how data flows along those sides helps you decide where to place your files and how to retrieve them later.

Imagine opening a fresh cloud instance. The instance is an empty desk: when you close it, the desk is cleared, and anything not packed away vanishes. To save your work, you must move it to another corner of the triangle before the instance shuts down.

## The Life of an Instance

A **cloud compute instance** is a virtual computer that you rent temporarily. Its hardware – CPUs, memory, and disk – comes from a pool of shared cloud resources. Software inside the instance is defined by a Docker container. The container ensures that everyone starts with the same tools and libraries, which keeps analyses reproducible.

Instances are **ephemeral**. When you stop an instance or it idles out, the virtual machine disappears. Any data that lived only on that instance is lost. Because of this, you should treat the instance as a workspace for computation rather than storage. Work with files there, but always push important results to GitHub or persistent storage before closing.

**Example:** Launch a notebook on your instance, generate figures, and commit the resulting image files before shutting it down.

> **Tip:** Make a habit of pushing commits or copying data off the instance at the end of each session to avoid losing work.

## Persistent Storage: The Long-Term Memory

**Persistent storage** is where you keep files that need to outlive the instance. CyVerse provides this storage, and it is ideal for datasets larger than 100 MB. The instance communicates with storage over HTTP, but that connection has a 2 GB limit. Within that limit, you can drag and drop files or use simple `push` and `pull` commands.

When files exceed 2 GB, use CyVerse's **gocmds** utility. Gocmds is a specialized transfer tool derived from the older `commands` interface. It can move large datasets efficiently between your instance and persistent storage, ensuring that big files make the trip safely.

**Example:** Keep a 10 GB reference genome in persistent storage and pull only the necessary chromosomes to your instance when needed.

> **Tip:** For long-term organization, mirror the folder structure of your GitHub repositories inside persistent storage.

## GitHub: Collaboration Hub and Record

**GitHub** is the collaboration hub for anything under 100 MB. It keeps a versioned history of your code, notebooks, and small data files, and it is the place where teams review changes and document their work. The organization leans heavily on GitHub, so repository templates are provided with a ready‑made GitHub Pages site. After you create a repository from a template, all you have to do is enable Pages to publish your documentation.

GitHub also ties into the authentication story. Today most instances authenticate with GitHub over SSH using keys and the `git@github.com:` address. Newer containers are transitioning to two‑factor authentication over HTTPS (`https://github.com/`). Anyone can clone a public repository via HTTPS, but pushing changes back requires authentication. With 2FA enabled, you supply a personal access token instead of a password when you push.

**Example:** Open a pull request to share a Jupyter notebook with colleagues and discuss revisions before merging.

> **Tip:** Use `.gitignore` to keep large or sensitive files out of your repository and track them in persistent storage instead.

## Moving Data Around the Triangle

- **Instance ↔ GitHub**  
  Use `git` to clone repositories onto the instance, commit your changes, and push them back. SSH keys provide seamless access once configured. With the shift to 2FA, expect to use HTTPS URLs and personal access tokens instead.
- **Instance ↔ Persistent Storage**  
  For small files (under 2 GB), the instance mounts your storage area over HTTP, so you can move files with a graphical drag‑and‑drop interface or with standard copy commands. For anything larger, launch **gocmds** to handle the transfer.
- **Persistent Storage ↔ GitHub**  
  Files that are too large for GitHub should live in persistent storage. In your repository, include scripts or metadata that reference those external files so collaborators know where to find them.

## A Day in the Life

1. **Start an instance.** CyVerse provisions a virtual machine and launches the appropriate Docker container so your software stack is ready.
2. **Clone your repository.** Use SSH or HTTPS to bring your GitHub project onto the instance.
3. **Work with data.** Pull datasets from persistent storage to the instance. Keep individual files under 2 GB if you are using the HTTP link; otherwise, rely on gocmds.
4. **Save your progress.** Commit and push code and small results back to GitHub. Copy large outputs to persistent storage so they survive when the instance shuts down.
5. **Shut down the instance.** The virtual machine disappears, but your work lives on in GitHub and persistent storage.

## Workflow Guidelines

- Treat the instance as temporary: never leave the only copy of a file there.
- Use GitHub for version‑controlled content under 100 MB.
- Rely on persistent storage for datasets and results that exceed GitHub's limits.
- Remember the 2 GB HTTP transfer cap between the instance and storage and switch to gocmds for larger transfers.
- Enable GitHub Pages in your repository template to share documentation and analyses with your team.

## Next Steps

By mastering the cloud triangle, you can move smoothly among compute resources, long‑term storage, and collaborative version control. The more comfortable you become with these paths, the easier it will be to keep your research organized, reproducible, and accessible.

