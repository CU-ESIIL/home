# Container Image Library

## Sell It
Pre-built container images give you ready-to-run environments without installing
software on your machine. They ensure your code runs the same on every system
and make sharing workflows straightforward.

## Show It
The [Container Image Library](../container-library/index.md) lists images with
descriptions and tags. Each entry links to a Docker or Apptainer image that you
can pull to see a fully configured environment.

## Do It
1. **Browse the library.** Look for an image that matches the tools you need.
2. **Pull the image.** Use `docker pull <image>` or
   `apptainer pull <image>` to download it.
3. **Run it.** Start the container with `docker run -it <image> /bin/bash` or
   the equivalent Apptainer command to open a shell inside the environment.
4. **Mount data.** Add `-v /path/to/data:/data` to access files from your
   machine inside the container.

## Review It
Check the tools and versions inside the container and note which images fit your
workflow. Reuse the image in future projects or use it as a base for your own
custom container.
