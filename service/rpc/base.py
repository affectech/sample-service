from typing import Optional
from pydantic import BaseModel


class RPCCall(BaseModel):
    jsonrpc: str
    method: str
    params: list[str] | None
    id: Optional[str]

class RPCError(BaseModel):
    code: int
    message: str
    data: Optional[dict[str, str]]

class RPCReply(BaseModel):
    jsonrpc: str
    result: Optional[dict[str, str]]
    error: RPCError | None
    id: str | None