# This web service uses FastAPI to accept requests to convert json files to a standard data structure
#
# The following modules are used in this service
# fastapi - Web service framework used to build the API
# pydantic - Parsing library used to easily parse the provided json data to the API
# typing - Primarliy using the Union function to handle optional json data passed to the API
# GenImage - Custom library used to manage the generated AI images and layer them for the final banner

from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
import shutil
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})


@app.post("/schema/")
def upload_file(file: UploadFile):
    if file.content_type != "application/json":
        raise HTTPException(400,detail="Invalid document type")
    else:
        data = json.loads(file.file.read())
    return {"content":data ,"filename":file.filename}