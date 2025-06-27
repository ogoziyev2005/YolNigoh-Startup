# Zichlik baholash formulalari
# utils/traffic_math.py
# Transport zichligi baholash formulalari (advanced scoring uchun)

def compute_density(vehicle_count: int, area_m2: float = 50.0) -> float:
    """
    Zichlikni m^2 ga nisbatan hisoblash (advanced versiya)
    """
    return round(vehicle_count / area_m2, 2)