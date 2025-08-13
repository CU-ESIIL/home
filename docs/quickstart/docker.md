# Starting Docker Containers

## Sell It
Docker packages your software and all of its dependencies into portable
containers that run the same way on laptops, servers, or the cloud. Instead of
configuring each machine manually, you capture the environment once and share
it with collaborators.

## Show It
A simple `Dockerfile` defines an environment. Each instruction adds a layer to
the final image so it can be rebuilt or modified easily:

```Dockerfile
FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
```

## Do It
1. **Install Docker.** Download Docker Desktop or the Docker Engine for your
   operating system from [docker.com](https://www.docker.com/).
2. **Create a project.** Make a folder with a `Dockerfile` like the example
   above or choose an existing image from Docker Hub.
3. **Build the image.** From the folder run `docker build -t myimage .` to turn
   the `Dockerfile` into a reusable image.
4. **Run the container.** Launch it with `docker run -it myimage /bin/bash` to
   open a shell inside the container.
5. **Share it.** Tag and push the image to a registry such as Docker Hub with
   `docker tag myimage myuser/myimage` followed by `docker push myuser/myimage`.

## Review It
Use `docker ps -a` to list containers and `docker images` to see available
images. Remove test containers with `docker rm` and clean up images with
`docker rmi` when you're done.
