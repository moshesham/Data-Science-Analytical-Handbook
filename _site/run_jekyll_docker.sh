#!/usr/bin/env bash
# Run this from the repo root in bash to start the Jekyll site inside Docker
PWD_HOST=$(pwd)
echo "Starting Jekyll (Docker) for project at: ${PWD_HOST}"
docker run --rm -it -v "${PWD_HOST}:/srv/jekyll" -p 4000:4000 -w /srv/jekyll jekyll/jekyll:4 jekyll serve --watch --force_polling --host 0.0.0.0 --port 4000
