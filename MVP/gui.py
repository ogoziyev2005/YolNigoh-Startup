# Transport oqimini GUI'da ko'rsatish (Streamlit versiyasi)
# gui.py
# Transport soni va svetafor vaqti vizual ko‘rinishda ko‘rsatiladi
# GUI texnologiyasi: Streamlit (engil va tez)

import streamlit as st
import time

st.set_page_config(page_title="YOLOv8 Transport Zichlik Monitor", layout="centered")
st.title("🚦 Real-time Transport Zichlik Monitoring")

placeholder = st.empty()

while True:
    try:
        with open("vehicle_count.txt", "r") as f:
            vehicle_count = int(f.read())
    except:
        vehicle_count = 0  # Fayl yo'q yoki noto‘g‘ri bo‘lsa

    green_time = vehicle_count * 1.5  # yoki: green_time = process_density(vehicle_count)

    with placeholder.container():
        st.write(f"### Aniqlangan transport vositalari soni: {vehicle_count}")
        st.write(f"## 🟢 Yashil chiroq davomiyligi: `{int(green_time)}` soniya")

    time.sleep(1)

