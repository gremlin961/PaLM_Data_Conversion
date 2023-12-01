# This web service uses FastAPI to accept requests to convert json files to a standard data structure
#
# The following modules are used in this service
# fastapi - Web service framework used to build the API
# uvicorn - ASGI web server implementation for Python
# json - Used to interact with json files and data passed to the web service
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

# Specify the location for the Jinja templates
templates = Jinja2Templates(directory="templates")

# Define the entry point for the service and render the UI using the "uploadfile.html" file
@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})

# The entrypoint used to process the parameters, template and data json files.
@app.post("/convert")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    # For loop used to verify the uploaded files are json
    for file in files:
        if file.content_type != "application/json":
            # If the uploaded file is not in json, return an error.
            raise HTTPException(400,detail="Invalid document type for file "+file.filename+". Only json files are allowed")

    # Load the content of the uploaded files        
    parameters = json.loads(files[0].file.read())
    template = json.loads(files[1].file.read())
    data = json.loads(files[2].file.read())

    # Pass the content of the uploaded files to the convert.GetData function 
    converted_data = convert.GetData(parameters, template, data)
    
    # Convert the returned data from the convert.GetData function to json and return it to the user
    json_response = json.loads(converted_data)
    return JSONResponse(content=json_response)
    
    # Comment out the previous return and uncomment the below line if you want to return the response as a string instead of json.
    #return converted_data
