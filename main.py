#! /usr/bin/env python3

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Server")


@app.get("/")
async def read_index_html():
    return FileResponse("index.html")


@app.get("/{title}.mp4")
async def read_movie(title: str):
    return FileResponse(f"{title}.mp4", media_type="video/mp4")


if __name__ == "__main__":
    from uvicorn import run

    run(
        app=f"{__name__}:app",
        host="127.0.0.1",
        log_level="info",
        port=8765,
        reload=True,
    )
