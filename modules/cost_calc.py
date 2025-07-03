import plotly.graph_objects as go

def run(p, v):
    construction = v["gross_floor"] * p["unit_cost"]
    demo_fee = v["gross_floor"]*p["demo_unit"]*0.3    # 拆除坪=總樓地板30%
    design_fee = construction * p["design_rate"]
    finance = (construction+demo_fee) * p["finance_rate"] * 1    # 1年
    misc = construction * 0.03
    total = sum([construction, demo_fee, design_fee, finance, misc])

    labels = ["營建費", "拆除費", "設計監造費", "融資利息", "其他"]
    values = [construction, demo_fee, design_fee, finance, misc]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.45)])
    fig.update_layout(showlegend=True)

    return dict(total_cost=total, pie_fig=fig)