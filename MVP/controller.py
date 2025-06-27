# Transport zichligini baholab, svetafor vaqtini hisoblash
# controller.py
# Ushbu modul transport vositalar soniga qarab svetafor vaqtini belgilaydi
# Manba: FarzadNekouee/YOLOv8_Traffic_Density_Estimation asosida optimallashtirilgan

def process_density(vehicle_count: int) -> int:
    """
    Berilgan transport vositalari soniga qarab svetaforning yashil chiroq davomiyligini belgilaydi.
    
    :param vehicle_count: Aniqlangan transport vositalar soni
    :return: Yashil chiroq yoqilishi kerak bo‘lgan soniya miqdori
    """
    if vehicle_count <= 5:
        return 5  # Past zichlik — qisqa yashil
    elif vehicle_count <= 10:
        return 10  # O‘rta zichlik
    elif vehicle_count <= 20:
        return 15  # Yuqori zichlik
    else:
        return 20  # Juda yuqori zichlik (tirbandlik) uchun maksimal vaqt