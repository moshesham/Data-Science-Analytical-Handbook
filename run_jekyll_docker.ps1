#!/usr/bin/env pwsh
# Run this from the repo root in PowerShell to start the Jekyll site inside Docker
$pwd = (Get-Location).Path
Write-Host "Starting Jekyll (Docker) for project at: $pwd"
docker run --rm -it -v "${pwd}:/srv/jekyll" -p 4000:4000 -w /srv/jekyll jekyll/jekyll:4 jekyll serve --watch --force_polling --host 0.0.0.0 --port 4000
