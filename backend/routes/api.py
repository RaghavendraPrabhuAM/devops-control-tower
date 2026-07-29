# Placeholder: API route definitions/blueprint for backend endpoints.
from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return {
        "message": "Hello Raghu! Bind Mount is Working",
        "status": "Running"
    }


@api.route("/health")
def health():
    return {
        "status": "Healthy",
        "service": "Backend API",
        "version": "1.0"
    }
@api.route("/info")
def info():
    return {
        "project": "DevOps Control Tower",
        "backend": "Flask",
        "version": "1.0.0",
        "environment": "Development",
        "author": "Raghu"
    }
@api.route("/hello")
def hello():
    return {
        "message": "Hello from Flask Backend!"
    }