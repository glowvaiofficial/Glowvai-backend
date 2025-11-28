import sys
sys.path.append("/opt/render/project/src/backend")
import os
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from skin_analyzer import analyze_skin

app = FastAPI()

# CORS (allows your frontend to call the backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create folder if missing
if not os.path.exists("backend/saved_images"):
    os.makedirs("backend/saved_images")


@app.get("/")
def root():
    return {"message": "Glowvai API is running!"}


@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    # Save image
    file_id = str(uuid.uuid4())
    file_path = f"backend/saved_images/{file_id}.jpg"

    with open(file_path, "wb") as f:
        f.write(await image.read())

    # Pass saved image to analyzer
    report = analyze_skin(file_path)

    return {
        "id": file_id,
        "original_filename": image.filename,
        "analysis": report
    }
