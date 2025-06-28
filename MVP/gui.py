# gui.py
import cv2
import streamlit as st
import time

import main



# Kamera ochish
cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera topilmadi yoki ishlamayapti.")
        break
    cap.release()
cv2.destroyAllWindows()



def gui_display(vehicle_count, green_signal_time):
    # Streamlit yordamida interfeysni yaratish
    st.set_page_config(page_title="YOLOv8 Transport Zichlik Monitor", layout="centered")
    st.title("🚦 Real-time Transport Zichlik Monitoring")

    placeholder = st.empty()

    with placeholder.container():
        st.write(f"### Aniqlangan transport vositalari soni: {vehicle_count}")
        st.write(f"## 🟢 Yashil chiroq davomiyligi: `{int(green_signal_time)}` soniya")


         # Video oqimini Streamlit interfeysiga chiqarish
    with placeholder.container():
        st.image(frame, channels="BGR", use_column_width=True)
        st.write(f"### Aniqlangan transport vositalari soni: {vehicle_count}")
        st.write(f"## 🟢 Yashil chiroq davomiyligi: `{green_signal_time}` soniya")


    time.sleep(1)








