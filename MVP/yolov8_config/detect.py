# YOLOv8 bilan aniqlash uchun konfiguratsiya
# yolov8_config/detect.py
# YOLOv8 modeli uchun maxsus konfiguratsiya moduli


def save_vehicle_count(count):
    with open("vehicle_count.txt", "w") as f:
        f.write(str(count))

        
def get_vehicle_count(model, frame, classes):
    results = model(frame)
    count = 0
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            if model.names[cls_id] in classes:
                count += 1
    return count





