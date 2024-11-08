from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import httpx
import os

SOROBAN_RPC_URL = os.getenv('SOROBAN_RPC_URL', 'https://mainnet.sorobanrpc.com')

async def health(request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                SOROBAN_RPC_URL,
                json={
                    "jsonrpc": "2.0",
                    "id": "0", 
                    "method": "getHealth",
                    "params": None
                },
                headers={
                    "Content-Type": "application/json"
                },
                timeout=3
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('result', {}).get('status') == 'healthy':
                    return JSONResponse({"healthy": True}, status_code=200)
            
            return JSONResponse({"healthy": False}, status_code=503)
            
    except Exception as e:
        return JSONResponse(
            {"healthy": False, "error": str(e)},
            status_code=503
        )


async def homepage(request):
    return JSONResponse({'hello': 'world'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/health', health),
])
