from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from main import generate_short_code, is_valid_url
from database import add_url, create_table

app = FastAPI()
from database import create_table

create_table()


class URL_Request(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/r/{code}")
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

@app.delete("/urls/{code}")
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

    code = generate_short_code({})

    add_url(code, request.url)

    return {"code": code, "url": request.url}