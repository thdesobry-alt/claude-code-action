#!/usr/bin/env python3
"""Serveur local de l'application Cannelures Laminoir.

Sert index.html et enregistre toutes les données dans laminoir-db.json
(dans le même dossier). Aucune dépendance : Python 3.8+ suffit.

    python serveur.py              # http://localhost:8080
    python serveur.py --port 9000  # autre port

Les autres postes du réseau ouvrent http://<nom-ou-IP-de-ce-poste>:8080
et travaillent sur la même base.
"""

import argparse
import json
import os
import re
import shutil
import threading
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "laminoir-db.json")
BACKUP_PATH = os.path.join(HERE, "laminoir-db.sauvegarde.json")
ID_RE = re.compile(r"^[A-Za-z0-9_.~:@+-]{1,200}$")
LOCK = threading.Lock()


def empty_db():
    return {
        "format": "laminoir-db",
        "version": 1,
        "config": {
            "options": [{"name": "Option 1"}, {"name": "Option 2"}, {"name": "Option 3"}],
            "paths": {},
            "procedures": {},
        },
        "cylinders": {},
    }


def read_db():
    if not os.path.exists(DB_PATH):
        return empty_db()
    with open(DB_PATH, encoding="utf-8") as f:
        db = json.load(f)
    db.setdefault("config", empty_db()["config"])
    db.setdefault("cylinders", {})
    return db


def write_db(db):
    """Écriture atomique ; l'ancienne version est gardée en sauvegarde."""
    db["updatedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    tmp = DB_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    if os.path.exists(DB_PATH):
        shutil.copyfile(DB_PATH, BACKUP_PATH)
    os.replace(tmp, DB_PATH)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def log_message(self, fmt, *args):
        if self.path.startswith("/api/") and self.command == "GET":
            return  # pas de bruit pour le rafraîchissement automatique
        super().log_message(fmt, *args)

    def send_json(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def read_body(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > 5_000_000:
            raise ValueError("corps de requête invalide")
        body = json.loads(self.rfile.read(length).decode("utf-8"))
        if not isinstance(body, dict):
            raise ValueError("un objet JSON est attendu")
        return body

    def do_GET(self):
        if self.path.split("?")[0] == "/api/db":
            with LOCK:
                return self.send_json(200, read_db())
        if self.path in ("/", ""):
            self.path = "/index.html"
        if self.path.split("?")[0] in ("/serveur.py", "/laminoir-db.json"):
            return self.send_json(404, {"error": "introuvable"})
        return super().do_GET()

    def do_PUT(self):
        parts = self.path.split("?")[0].strip("/").split("/")
        try:
            body = self.read_body()
        except ValueError as e:
            return self.send_json(400, {"error": str(e)})
        with LOCK:
            db = read_db()
            if parts == ["api", "db"]:
                # Import d'une base complète.
                if not isinstance(body.get("cylinders"), dict) or not isinstance(body.get("config"), dict):
                    return self.send_json(400, {"error": "base invalide"})
                db = {**empty_db(), "config": body["config"], "cylinders": body["cylinders"]}
            elif parts == ["api", "config", "main"]:
                db["config"] = body
            elif len(parts) == 3 and parts[:2] == ["api", "cylinders"] and ID_RE.match(parts[2]):
                body["id"] = parts[2]
                db["cylinders"][parts[2]] = body
            else:
                return self.send_json(404, {"error": "introuvable"})
            write_db(db)
        return self.send_json(200, {"ok": True})

    def do_DELETE(self):
        parts = self.path.split("?")[0].strip("/").split("/")
        if len(parts) == 3 and parts[:2] == ["api", "cylinders"] and ID_RE.match(parts[2]):
            with LOCK:
                db = read_db()
                db["cylinders"].pop(parts[2], None)
                write_db(db)
            return self.send_json(200, {"ok": True})
        return self.send_json(404, {"error": "introuvable"})


def main():
    parser = argparse.ArgumentParser(description="Serveur Cannelures Laminoir")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--host", default="0.0.0.0", help="0.0.0.0 = accessible depuis le réseau")
    args = parser.parse_args()
    if not os.path.exists(DB_PATH):
        write_db(empty_db())
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Cannelures Laminoir : http://localhost:{args.port}")
    print(f"Base de données : {DB_PATH}")
    print("Ctrl+C pour arrêter.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
