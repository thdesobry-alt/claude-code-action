#!/bin/sh
# Lance le serveur Cannelures Laminoir.
cd "$(dirname "$0")"
exec python3 serveur.py "$@"
