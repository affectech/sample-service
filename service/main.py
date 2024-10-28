from typing import Union, Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class RPCCall(BaseModel):
    jsonrpc: str
    method: str
    params: Optional[list[str]]
    id: Optional[str]

@app.get("/endpoint")
def read_endpoint():
    return {"Hello": "Endpoint"}

@app.post("/rpc")
def read_rpc_call(call: RPCCall):
    return call 