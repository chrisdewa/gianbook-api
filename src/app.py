from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/ping')
async def get_ping() -> str:
    """Simple get to check app status"""
    return 'pong'

