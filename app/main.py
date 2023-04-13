from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"From: {os.environ.get('HOSTNAME', 'Unable to fetch Hostname')} ENV: {os.environ.get('ENV', 'Unable to fetch ENV')}"}