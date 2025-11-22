# Running the site locally with Docker

This repository includes a Docker Compose configuration and simple helper scripts to run the Jekyll site inside a container so you don't need to install Ruby/Bundler locally.

Requirements
- Docker Desktop (or Docker Engine) installed and running.

Start with Docker Compose (recommended)

PowerShell / CMD / bash (from repo root):

```bash
docker-compose up
```

Then open: http://localhost:4000

Run with the helper script (PowerShell)

```powershell
.\run_jekyll_docker.ps1
```

Or with the bash helper:

```bash
./run_jekyll_docker.sh
```

Notes
- The container mounts the repository into `/srv/jekyll`, so changes you make locally are reflected in the running site.
- If you need to install additional gems, add them to `Gemfile` and rebuild (or run `bundle install` inside the container).
- If your Docker host is WSL, mapping may already work; on Windows-native Docker you may need to grant file sharing permissions for the repo path.
