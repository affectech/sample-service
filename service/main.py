from fastapi import FastAPI

from .rpc import RPCCall, RPCReply

app = FastAPI()

@app.get("/endpoint")
def read_endpoint():
    return {"Hello": "Endpoint"}

@app.post("/rpc", response_model=RPCReply)
def read_rpc_call(call: RPCCall):
    return RPCReply(
        jsonrpc="2.0", 
        result={"hello": "world"}, 
        error=None, 
        id=call.id
    ) 