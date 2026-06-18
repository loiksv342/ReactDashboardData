from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import StringIO

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chart-data")
async def chart(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Only CSV allowed")

    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode("utf-8")))

    if df.shape[1] < 2:
        raise HTTPException(status_code=400, detail="Need at least 2 columns")

    x = df.iloc[:, 0].astype(str)
    y = df.iloc[:, 1]

    return {
        "labels": x.tolist(),
        "values": y.tolist()
    }