# Starting Docker Containers

## Sell It
Docker packages software and dependencies into portable containers that run consistently anywhere.

## Show It
A simple `Dockerfile` defines an environment:

```Dockerfile
FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
```

## Do It
1. Install [Docker](https://www.docker.com/) for your operating system.
2. Create a `Dockerfile` like the example above or pull an existing image.
3. Build it with `docker build -t myimage .`.
4. Run the container using `docker run -it myimage`.

## Review It
List containers with `docker ps` to confirm it ran and note how reproducible the environment is for future projects.
