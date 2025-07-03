import plotly.graph_objects as go

def run(p, c, r):
    owner_value = (r["total_revenue"] - c["total_cost"]) * p["right_ratio"]
    return_area = owner_value / p["unit_price"]
    impl_value = r["total_revenue"] - owner_value
    fig = go.Figure()
    fig.add_bar(x=["地主", "實施者"], y=[owner_value, impl_value])
    fig.update_yaxes(title="價值(元)")
    return dict(owner_value=owner_value, bar_fig=fig,
                return_area=return_area)