from fastapi import FastAPI

app = FastAPI()


@app.get("/getObjects")
async def root():
    return {"message": "Hello World"}

