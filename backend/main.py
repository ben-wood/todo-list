from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files from the root path
app.mount("/", StaticFiles(directory="static", html=True), name="static")
