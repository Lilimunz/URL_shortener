from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import starlette.status as status

import core


app = FastAPI()

@app.post("/create")
def create_url(url):
    id = core.create_url(url)
    return {
        'url': url,
        'id': id
    }

@app.get("/{id}")
def search_url(id):
    url = core.search_url(id)

    if not url:
        raise HTTPException(status_code=403, detail="Item not found")

    if "http" not in url:
        url = f"http://{url}"
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
