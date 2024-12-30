from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 
from typing import List,Dict,Any
    
# Create a FastAPI instance
app = FastAPI()

# Initialize variables to store uploaded data
raw_data = None
processed_data = None

# Define Upload endpoint
@app.post("/upload/{type}",
          summary="Upload Data",
          description="Upload Raw or Processed Data to the API")
async def upload(type:str,data:Dict[str,Any]):
    if type not in ["raw","processed"]:
        raise HTTPException(status_code=404,detail="Invalid Type")
    if type == "raw":
        global raw_data
        raw_data = data["content"]
    else:
        global processed_data
        processed_data = data["content"]
        
    raise HTTPException(status_code=200,detail="Upload Data Successfully")

# Define Download endpoint
@app.get("/download/{type}",
         summary="Download Data",
         description="Download Raw or Processed Data from the API")
async def download(type:str):
    if type not in ["raw","processed"]:
        raise HTTPException(status_code=404,detail="Invalid Type")
    
    if type == "raw":
        if raw_data is None:
            raise HTTPException(status_code=404,detail="No Raw Data Uploaded")   
        return raw_data
    else:
        if processed_data is None:
            raise HTTPException(status_code=404,detail="No Processed Data Uploaded")   
        return processed_data