from datetime import datetime
from fastapi import FastAPI,HTTPException,Request
from typing import Any
from random import randint

app=FastAPI(root_path='/api/v1')

data:Any=[
    {"campaign_id":1,"name":"Summer Launch","due_date":datetime.now(),"created_at":datetime.now()},
    {"campaign_id":2,"name":"Black Friday","due_date":datetime.now(),"created_at":datetime.now()},
]

@app.get('/')
async def root():
    return {'message':'Hello world'}

@app.get('/campaigns')
async def read_campaign():
    return {'campaign':data}

@app.get('/campaigns/{id}')
async def read_campaign(id:int):
    for campaign in data:
        if campaign.get('campaign_id')==id:
            return {'campaign':campaign}
    raise HTTPException(status_code=404)

@app.post('/campaigns')
async def create_campaigns(body:dict[str,Any]):

    new:Any={
        "campaign_id":randint(100,1000),
        "name":body.get('name'),
        "due_date":body.get('due_date'),
        "created_at":datetime.now()
    }
    
    data.append(new)
    return {'campaign':new}