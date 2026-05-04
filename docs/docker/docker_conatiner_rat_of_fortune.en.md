# Rat of Fortune Docker Image

# docker_container_rat-of-fortune

Rat of Fortune is a small browser-based application that spins a graphical wheel to pick a random name from a list.

It is useful for lightweight demos, team games, random assignment, or any situation where a visual random picker is more fun than a script.

## Image

- Docker Hub: [bsmeding/rat-of-fortune](https://hub.docker.com/repository/docker/bsmeding/rat-of-fortune/general)
- Source: [docker_container_rat-of-fortune](https://github.com/bsmeding/docker_container_rat-of-fortune)
- Demo: [Rat of Fortune](https://netdevops.it/wheel/)
- Port: `5000`

## Features

- Load names from a `names.txt` file
- Select which users to include with checkboxes
- Spin a graphical wheel in the browser
- Show an animated winner announcement
- Run behind a reverse proxy using a configurable base path

## Docker run

Create a name list:

```bash
printf "Alice\nBob\nCharlie\nDiana\n" > names.txt
```

Start the container:

```bash
docker run -p 5000:5000 \
  -v $(pwd)/names.txt:/app/names.txt \
  bsmeding/rat-of-fortune:latest
```

Open the application at `http://localhost:5000/`.

## Run under a subpath

Set `APP_BASE_PATH` when the application is published behind a reverse proxy path such as `/wheel`.

```bash
docker run -p 5000:5000 \
  -v $(pwd)/names.txt:/app/names.txt \
  -e APP_BASE_PATH=/wheel \
  bsmeding/rat-of-fortune:latest
```

Open the application at `http://localhost:5000/wheel/`.

## Build from source

```bash
git clone https://github.com/bsmeding/docker_container_rat-of-fortune.git
cd docker_container_rat-of-fortune

printf "Alice\nBob\nCharlie\nDiana\n" > names.txt

docker build -t rat-of-fortune .
docker run -p 5000:5000 \
  -v $(pwd)/names.txt:/app/names.txt \
  rat-of-fortune
```

## Credits

- Winwheel.js for the wheel logic
- GSAP TweenMax for animation
