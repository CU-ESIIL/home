# Starting with GitHub

## Sell It
GitHub is more than a place to store code. It provides version control,
collaboration tools, and a central home for project documentation. By keeping
your work on GitHub you get an online backup, the ability to rewind to any
previous version, and a simple way to work with teammates regardless of where
they live.

## Show It
Open a repository page on GitHub and you will see the source files, commit
history, branches, and an issue tracker. The **Code** tab lists your files, the
**Issues** tab records bugs and ideas, and **Pull Requests** is where proposed
changes are discussed before they are merged.

## Do It
1. **Create an account.** Sign up for a free account at
   [GitHub](https://github.com/).
2. **Install Git.** Download and install [Git](https://git-scm.com/). On first
   run, set your name and email:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. **Make a repository.** On GitHub click *New* to create a repository, then
   clone it to your computer with `git clone <url>`.
4. **Track a change.** Inside the repository add a file such as `README.md`,
   run `git add README.md`, and commit with `git commit -m "Add README"`.
5. **Share it.** Push your work with `git push origin main` and refresh the page
   on GitHub to see your commit.

## Review It
Confirm the commit appears on GitHub and explore the **Issues** and **Pull
Requests** tabs. Invite a collaborator to open an issue or suggest a change so
you can practice reviewing and merging their work.
