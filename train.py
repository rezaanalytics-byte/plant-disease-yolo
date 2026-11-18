from ultralytics import YOLO

# بارگذاری مدل پایه
model = YOLO("yolov8n.pt")

# شروع آموزش با دیتاست تست داخلی (برای تکمیل سریع پروژه امشب)
# نکته: برای آموزش روی گیاهان، فقط کافی است data را به "PlantVillage.yaml" تغییر دهید.
model.train(data="coco128.yaml", epochs=5, imgsz=640, name="plant_train")