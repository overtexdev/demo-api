from fastapi import FastAPI
import os
import socket

app = FastAPI(title="Demo API - Homelab CI/CD")


@app.get("/")
def read_root():
    return {
        "message": "Déployé automatiquement via CI/CD sur le homelab",
        "host": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "dev"),
    }


@app.get("/health")
def health():
    return {"status": "ok"}
