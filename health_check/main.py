import asyncio
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import httpx
import os

SOROBAN_RPC_URL = os.getenv("SOROBAN_RPC_URL", "https://mainnet.sorobanrpc.com")


async def get_health_info():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SOROBAN_RPC_URL,
            json={"jsonrpc": "2.0", "id": "0", "method": "getHealth", "params": None},
            headers={"Content-Type": "application/json"},
            timeout=3,
        )
        return response


async def health(request):
    try:
        response = await get_health_info()
        if response.status_code == 200:
            data = response.json()
            if data.get("result", {}).get("status") == "healthy":
                return JSONResponse({"healthy": True}, status_code=200)

        return JSONResponse({"healthy": False}, status_code=503)

    except Exception as e:
        return JSONResponse({"healthy": False, "error": str(e)}, status_code=503)


async def homepage(request):
    return JSONResponse({"hello": "world"})


async def on_shutdown():
    print("Stopping the app, wait for 10 seconds")
    await asyncio.sleep(10)
    print("App stopped")


async def on_startup():
    current_ledger = -1
    while True:
        try:
            response = await get_health_info()
            if response.status_code != 200:
                continue
            data = response.json()
            if data.get("result", {}).get("status") != "healthy":
                continue
            if current_ledger == -1:
                current_ledger = data.get("result", {}).get("latestLedger")
                if current_ledger is None:
                    continue
                print(f"Current ledger: {current_ledger}")
            else:
                if current_ledger != data.get("result", {}).get("latestLedger"):
                    print("Ledger changed")
                    break
            await asyncio.sleep(1)
        except Exception as e:
            continue
    await asyncio.sleep(3)
    print("App started")


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/health", health),
    ],
    on_shutdown=[on_shutdown],
    on_startup=[on_startup],
)
