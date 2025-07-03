import streamlit as st
from modules import (
    input_sidebar, volume_calc, cost_calc,
    revenue_calc, allocation_calc, sensitivity
)

st.set_page_config(page_title="都市更新權利變換試算",
                   layout="wide",
                   page_icon="🏙️")

# -------- Sidebar -------- #
params = input_sidebar.show()

# -------- 核心計算 -------- #
volume = volume_calc.run(params)
costs = cost_calc.run(params, volume)
revenues = revenue_calc.run(params, volume)
allocation = allocation_calc.run(params, costs, revenues)
sen_data = sensitivity.run(params)

# -------- Page Tabs -------- #
tab1, tab2, tab3 = st.tabs(["📊 模型試算", "🕸️ 敏感度分析", "📄 操作說明"])

with tab1:
    st.subheader("關鍵指標 (KPI)")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("總可建坪", f"{volume['gross_floor']:.0f} 坪")
    k2.metric("可售建坪", f"{volume['saleable_floor']:.0f} 坪")
    k3.metric("總開發成本", f"{costs['total_cost']/1e8:.2f} 億元") 
    k4.metric("地主可分配價值", f"{allocation['owner_value']/1e6:.2f} 百萬元")

    st.plotly_chart(costs["pie_fig"], use_container_width=True)
    st.plotly_chart(allocation["bar_fig"], use_container_width=True)

with tab2:
    st.subheader("敏感度分析")
    st.plotly_chart(sen_data["radar_fig"], use_container_width=True)

with tab3:
    st.markdown(open("README.md", "r", encoding="utf-8").read())