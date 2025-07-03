def run(p):
    legal_p = p["land_area"] * p["legal_far"]
    reward_p = p["land_area"] * p["ori_far"] * 1.5   # 防災2.0
    gross_p = max(legal_p, reward_p)
    gross_floor = gross_p / 3.3          # 坪化
    saleable = gross_floor * p["sale_coef"]
    return dict(gross_floor=gross_floor, saleable_floor=saleable)