import pandas as pd
import plotly.graph_objects as go
from modules import volume_calc, revenue_calc, cost_calc, allocation_calc

def run(p):
    factors = {
        "營建單價": ("unit_cost", p["unit_cost"]),
        "市場單價": ("unit_price", p["unit_price"]),
        "可售係數": ("sale_coef", p["sale_coef"])
    }
    results = []
    for f, (key, val) in factors.items():
        for sign, ratio in [("-", 0.9), ("0", 1.0), ("+", 1.1)]:
            new_p = p.copy()
            new_p[key] = val * ratio
            vol = volume_calc.run(new_p)
            rev = revenue_calc.run(new_p, vol)
            cost = cost_calc.run(new_p, vol)
            alloc = allocation_calc.run(new_p, cost, rev)
            results.append(dict(
                指標=f"{f}{sign}",
                地主分配坪數=alloc["return_area"]
            ))
    df = pd.DataFrame(results)
    fig = go.Figure()
    for f in df["指標"].str[:-1].unique():
        subset = df[df["指標"].str.contains(f)]
        fig.add_trace(go.Scatterpolar(
            r=subset["地主分配坪數"],
            theta=subset["指標"],
            fill='toself',
            name=f
        ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)))
    return dict(radar_fig=fig)