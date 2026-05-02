from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from main import load_urls, save_urls, generate_short_code,is_valid_url

app = FastAPI()

urls = load_urls()

class URL_Request(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/r/(code)")
def redirect_url(code: str):
    if code not in urls:
        raise HTTPException(status_code=404, detail="URL not found")

    urls[code]["clicks"] += 1
    save_urls(urls)

    return RedirectResponse(urls[code]["url"])


@app.get("/url/{code}")
def get_url(code: str):

    if code not in urls:
        raise HTTPException(status_code=404, detail="URL not found")

    urls[code]["clicks"] += 1
    save_urls(urls)

    return urls[code]

@app.post("/url/{code}")
def delete_url(code: str):
    if code not in urls:
        raise HTTPException(status_code=404, detail="URL not found")

    del urls[code]
    save_urls(urls)

    return {"message": "URL deleted successfully"}



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