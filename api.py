from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from main import load_urls, save_urls, generate_short_code,is_valid_url

app = FastAPI()

urls = load_urls()

class URL_Request(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/urls")
def list_urls():
    return urls
@app.post("/shorten")
def shorten_url(request: URL_Request):

    if not is_valid_url(request.url):
        raise HTTPException(status_code=400, detail="Invalid URL. Must start with http:// or https://")

    code = generate_short_code(urls)

    urls[code] = {
        "url": request.url,
        "clicks": 0
    }

    save_urls(urls)

    return {"code": code, "url": request.url}