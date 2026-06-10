from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from main import generate_short_code, is_valid_url
from database import (
    add_url,
    create_table,
    get_all_urls,
    get_url_by_code,
    increment_clicks,
    delete_url_db
)

app = FastAPI()

create_table()


class URL_Request(BaseModel):
    url: str

@app.get("/")
def home() -> dict:
    return {"message": "API is working"}

@app.get("/r/{code}")
def redirect_url(code: str):
    row = get_url_by_code(code)

    if row is None:
        raise HTTPException(status_code=404, detail="URL not found")
    increment_clicks(code)
    return RedirectResponse(url=row[1])


@app.get("/url/{code}")
def get_url(code: str):

    row = get_url_by_code(code)

    if row is None:
        raise HTTPException(
            status_code = 404,
            detail = "URL not found"
        )

    increment_clicks(code)

    return {
        "success": True,
        "data": {
            "code": row[0],
            "url": row[1],
            "clicks": row[2] + 1
        }
    }

@app.delete("/urls/{code}")
def delete_url(code: str):

   row = get_url_by_code(code)
   if row is None:
       raise HTTPException(status_code=404, detail="URL not found")

   delete_url_db(code)

   return {
       "success": True,
       "message": "URL deleted successfully"
   }


@app.get("/urls")
def get_urls() -> dict:

    rows = get_all_urls()

    result = []

    for code, url, clicks in rows:
        result.append({
            "code": code,
            "url": url,
            "clicks": clicks
        })

    return {
        "success": True,
        "count": len(result),
        "data": result
    }

@app.post("/shorten")
def shorten_url(request: URL_Request) -> dict:

    if not is_valid_url(request.url):
        raise HTTPException(status_code=400, detail="Invalid URL. Must start with http:// or https://")

    code = generate_short_code()

    add_url(code, request.url)

    return {
        "success": True,
        "message": "URL shortened successfully",
        "data": {
            "code": code,
            "url": request.url
        }
    }