import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI(
    default_response_class=HTMLResponse,
)


@app.get("/")
def index():
    return "<h1>Hello there 👋</h1>"


if __name__ == "__main__":
    host: str = os.environ.get("APP_HOST", "0.0.0.0")
    port: int = int(os.environ.get("APP_PORT", 8000))
    debug: bool = bool(os.environ.get("APP_DEBUG", False))
    uvicorn.run(app, host=host, port=port, debug=debug)  # type: ignore
