from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from datetime import datetime
from backend.services.analyze_csv import analyze_trades

router = APIRouter()

UPLOAD_DIR = "data/uploads"

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(UPLOAD_DIR, today)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    result_path = analyze_trades(file_path, folder_path)
    return {"message": "File uploaded and analyzed", "analysis_file": result_path}
