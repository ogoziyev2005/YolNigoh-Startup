# Jetson kamera yoki USB kamera konfiguratsiyasi
# utils/camera.py
# Jetson CSI va USB kamera interfeysi moduli

import cv2

def get_camera(use_jetson=False):
    if use_jetson:
        return cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    else:
        return cv2.VideoCapture(0)