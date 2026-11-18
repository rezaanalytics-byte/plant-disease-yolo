from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI(title="Plant Disease Detection API", version="1.0.0")

# بارگذاری مدل (اگر مدل آموزش‌دیده نداری، از مدل پایه استفاده می‌کند)
try:
    model = YOLO("best.pt")
except:
    print("⚠️ مدل best.pt پیدا نشد. از مدل پایه YOLOv8n استفاده می‌شود.")
    model = YOLO("yolov8n.pt")

@app.get("/")
def root():
    return {"message": "Plant Disease Detection API is running! 🌿"}

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    # خواندن تصویر
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # اجرای مدل
    results = model.predict(source=img, conf=0.5, verbose=False)
    
    detections = []
    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            raw_name = model.names[cls_id]
            conf = float(box.conf[0])
            
            # تمیز کردن نام کلاس (مثلاً تبدیل Tomato___Late_blight به Tomato - Late blight)
            clean_name = raw_name.replace('___', ' - ').replace('_', ' ').title()
            
            detections.append({
                "disease": clean_name,
                "confidence": round(conf, 3)
            })
            
    return JSONResponse(content={"detections": detections})