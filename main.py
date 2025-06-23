# main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="/code")

@app.get("/", response_class=HTMLResponse)
def form_post(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
