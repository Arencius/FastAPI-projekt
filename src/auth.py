from datetime import datetime
from src.secret import API_KEY
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends, APIRouter
from fastapi.security.api_key import APIKey
from starlette.status import HTTP_403_FORBIDDEN


api_key_header = APIKeyHeader(name="access_token", auto_error=False)
auth_router = APIRouter()


async def get_api_key(header: str = Security(api_key_header)):
    if header == API_KEY:
        return header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


@auth_router.get("/get_time")
async def get_time(api_key: APIKey = Depends(get_api_key)):
    return datetime.now().strftime('%H:%M:%S')
