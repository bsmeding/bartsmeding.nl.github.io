# Rat of Fortune Docker-image

# docker_container_rat-of-fortune

Rat of Fortune is een kleine browsergebaseerde applicatie die een grafisch rad laat draaien om willekeurig een naam uit een lijst te kiezen.

De image is handig voor demo's, teamspellen, willekeurige toewijzing of situaties waarin een visuele random picker leuker is dan een script.

## Image

- Docker Hub: [bsmeding/rat-of-fortune](https://hub.docker.com/repository/docker/bsmeding/rat-of-fortune/general)
- Broncode: [docker_container_rat-of-fortune](https://github.com/bsmeding/docker_container_rat-of-fortune)
- Demo: [Rat of Fortune](https://netdevops.it/wheel/)
- Poort: `5000`

## Features

- Namen laden uit een `names.txt`-bestand
- Gebruikers selecteren met checkboxes
- Een grafisch rad draaien in de browser
- Een geanimeerde winnaar tonen
- Draaien achter een reverse proxy met een configureerbaar basispad

## Docker run

Maak een namenlijst:

```bash
printf "Alice\nBob\nCharlie\nDiana\n" > names.txt
```

Start de container:

```bash
docker run -p 5000:5000 \
  -v $(pwd)/names.txt:/app/names.txt \
  bsmeding/rat-of-fortune:latest
```

Open de applicatie via `http://localhost:5000/`.

## Draaien onder een subpath

Gebruik `APP_BASE_PATH` wanneer de applicatie achter een reverse-proxy-pad zoals `/wheel` wordt gepubliceerd.

```bash
docker run -p 5000:5000 \
  -v $(pwd)/names.txt:/app/names.txt \
  -e APP_BASE_PATH=/wheel \
  bsmeding/rat-of-fortune:latest
```

Open de applicatie via `http://localhost:5000/wheel/`.

## Bouwen vanuit broncode

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

- Winwheel.js voor de wiel-logica
- GSAP TweenMax voor animatie
