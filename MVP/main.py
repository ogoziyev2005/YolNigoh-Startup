import cv2
import numpy as np
from ultralytics import YOLO
from controller import process_density

# YOLOv8 modelini yuklash
model = YOLO('MVP/yolov8_config/yolov8s.pt')

# Kamera ochish
cap = cv2.VideoCapture(0)

vehicle_classes = ['car', 'bus', 'truck', 'motorbike']

# Masofa hisoblash uchun parametrlar
max_distance = 1000  # Maksimal masofa (pixellar)
min_distance = 200   # Minimal masofa (pixellar)

def save_vehicle_count(count):
    with open("vehicle_count.txt", "w") as f:
        f.write(str(count))

def calculate_traffic_intensity(vehicle_count):
    # Agar avtomobillar soni belgilangan thresholddan yuqori bo'lsa, "Heavy", aks holda "Smooth"
    heavy_traffic_threshold = 15
    yuqori_avtomobil= 40
    juda_past = 5
    Avtomobil_yuq = 0
    if vehicle_count > heavy_traffic_threshold:
        return "Yuqori"
    elif Avtomobil_yuq == vehicle_count:
        return "Avtomobil Yo'q"
    elif juda_past > vehicle_count:
        return "Juda past"
    elif yuqori_avtomobil < vehicle_count:
        return "O'ta Yuqori"
    else:
        return "O'rtacha"

def adjust_green_signal(traffic_intensity):
    if traffic_intensity == "Yuqori":
        return 30  # Heavy trafik uchun uzunroq yashil chiroq (masalan, 30 soniya)
    elif traffic_intensity == "Avtomobil Yo'q":
        return 0
    elif traffic_intensity == "Juda past":
        return 5        
    elif traffic_intensity == "O'ta Yuqori":
        return 60
    else:
        return 15  # Smooth trafik uchun qisqaroq yashil chiroq (masalan, 15 soniya)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera topilmadi yoki ishlamayapti.")
        break

    # YOLOv8 modelini ishlatish
    results = model(frame)
    vehicle_count = 0
    traffic_intensity = ""

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            if cls_name in vehicle_classes:
                vehicle_count += 1

                # Avtomobilning to'liq qutilarini olish
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                
                # Masofa hisoblash (kameraning markazi bilan)
                center_distance = np.sqrt(center_x**2 + center_y**2)  # Kamera markazidan masofa

                # Yashil chiroqni moslashtirish (masofaga qarab)
                if center_distance < min_distance:
                    # Masofa qisqa bo'lsa, avtomobilga tezroq ruxsat berish
                    green_time = 15  # Tez yashil chiroq
                elif center_distance < max_distance:
                    green_time = 25  # O'rta masofa uchun yashil chiroq
                else:
                    green_time = 35  # Uzoq masofa uchun uzun yashil chiroq

                # Ramka va nom yozish
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, cls_name, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Traffic intensity va green signal time
    traffic_intensity = calculate_traffic_intensity(vehicle_count)
    green_signal_time = adjust_green_signal(traffic_intensity)

    # Ekranda avtomobil soni va svetofor holatini ko'rsatish
    cv2.putText(frame, f"Avtomobil Soni: {vehicle_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Yashil chiroqni yashil rangda ko'rsatish
    if traffic_intensity == "Yuqori":
        cv2.putText(frame, f"🟢 Yashil chiroq: {green_signal_time}s", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Yashil rangda
    else:
        cv2.putText(frame, f"Yashil chiroq: {green_signal_time}s", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Yashil rangda

    # Ekranda trafik intensivligini ko'rsatish
    cv2.putText(frame, f"Tirbandlik Holati: {traffic_intensity}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 255), 2)

    # Natijani ko‘rsatish
    cv2.imshow("YOLOv8 Real-Time Detection", frame)

    if cv2.waitKey(1) == 27:  # ESC tugmasi
        break

cap.release()
cv2.destroyAllWindows()
