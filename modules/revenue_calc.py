def run(p, v):
    total_value = v["saleable_floor"] * p["unit_price"] * p["scenario"]
    return dict(total_revenue=total_value)