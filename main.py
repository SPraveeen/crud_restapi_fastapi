from datetime import datetime
from typing import Any
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return {"message":"Hi welcome"}

data:Any=[
    {
        "campaign_id":1,
        "name":"Summer Launch",
        "due_date":datetime.now(),
        "created_at":datetime.now()
    },
    {
        "campaign_id":2,
        "name":"Black Friday",
        "due_date":datetime.now(),
        "created_at":datetime.now()   
    }
]

@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns":"example"}