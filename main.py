# This web service uses FastAPI to accept requests to convert json files to a standard data structure
#
# The following modules are used in this service
# fastapi - Web service framework used to build the API
# pydantic - Parsing library used to easily parse the provided json data to the API
# typing - Primarliy using the Union function to handle optional json data passed to the API
# convert - Custom library used to submit form data to the PaLM text-bison model

from fastapi import FastAPI, File, UploadFile, Request, HTTPException
import uvicorn
import shutil
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import json
from typing import List
from pkg import convert


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})


@app.post("/convert")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    for file in files:
        if file.content_type != "application/json":
            raise HTTPException(400,detail="Invalid document type for file "+file.filename+". Only json files are allowed")
            
    parameters = json.loads(files[0].file.read())
    template = json.loads(files[1].file.read())
    data = json.loads(files[2].file.read())

    converted_data = convert.GetData(parameters, template, data)
    
    json_response = json.loads(converted_data)
    print(type(json_response))

    return JSONResponse(content=json_response)
    #return converted_data
