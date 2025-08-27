from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from starlette.responses import JSONResponse

app = FastAPI()
model = YOLO('best.pt')  # Replace with your YOLOv8 weights path

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    results = model(contents)
    detections = results[0].boxes.xyxy.tolist()  # bounding boxes
    classes = results[0].boxes.cls.tolist()       # class IDs
    confidences = results[0].boxes.conf.tolist()  # scores
    return JSONResponse({"boxes": detections, "classes": classes, "confidences": confidences})
