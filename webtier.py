from typing import Union
import csv
from fastapi import FastAPI, UploadFile, File
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# Load data on application startup
@app.on_event("startup")
async def load_data():
    global loaded_data
    try:
        with open('data.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            loaded_data = {}
            for row in csv_reader:
                if len(row) == 2:
                    key, value = row
                    loaded_data[key] = value
                else:
                    print(f"Ignoring invalid row: {row}")
            print(loaded_data)
    except FileNotFoundError:
        loaded_data = {}
        print("Data file not found. Initializing empty data.")


@app.post("/")
async def post_root(inputFile: UploadFile = File(...)):
    global loaded_data
    filename = inputFile.filename
    filename = filename.split('.')[0]
    print(filename)
    if filename not in loaded_data:
        raise HTTPException(status_code=404, detail="File not found in loaded data.")
    prediction_result = loaded_data[filename]
    return filename + ":" + prediction_result