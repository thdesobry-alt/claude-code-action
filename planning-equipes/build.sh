#!/bin/sh
# Génère index.html (page autonome, données dans le navigateur) à partir de planning.html,
# la source publiée telle quelle comme artefact claude.ai.
cd "$(dirname "$0")"
{
  printf '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n</head>\n<body style="margin:0">\n'
  cat planning.html
  printf '\n</body>\n</html>\n'
} > index.html
