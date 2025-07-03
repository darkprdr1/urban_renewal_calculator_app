import streamlit as st

def show():
    st.sidebar.title("輸入參數")

    land_area = st.sidebar.number_input("土地面積 (m²)", 10.0, 10000.0, 300.0)
    legal_far = st.sidebar.number_input("法定容積率 (%)", 50.0, 1000.0, 225.0)
    ori_far = st.sidebar.number_input("原建築容積率估算 (%)", 50.0, 600.0, 300.0)
    sale_coef = st.sidebar.slider("可售係數", 0.5, 0.9, 0.75, 0.01)

    st.sidebar.markdown("---")
    unit_cost = st.sidebar.number_input("營建單價 (元/坪)", 90000, 300000, 150000, 1000)
    demo_unit = st.sidebar.number_input("拆除單價 (元/坪)", 1000, 8000, 4000, 100)
    design_rate = st.sidebar.slider("設計監造率 (%)", 5.0, 15.0, 10.0, 0.5)
    finance_rate = st.sidebar.slider("融資利率 (%)", 2.0, 8.0, 3.0, 0.1)

    st.sidebar.markdown("---")
    unit_price = st.sidebar.number_input("市場單價 (萬元/坪)", 20.0, 120.0, 55.0, 0.5)
    scenario = st.sidebar.selectbox("情境係數", ["悲觀 0.9", "基準 1.0", "樂觀 1.1"])

    right_ratio = st.sidebar.slider("地主權利價值比率 (%)",
                                    50.0, 90.0, 70.0, 1.0)
    return dict(
        land_area=land_area,
        legal_far=legal_far/100,
        ori_far=ori_far/100,
        sale_coef=sale_coef,
        unit_cost=unit_cost,
        demo_unit=demo_unit,
        design_rate=design_rate/100,
        finance_rate=finance_rate/100,
        unit_price=unit_price*10000,
        scenario=float(scenario.split()[1]),
        right_ratio=right_ratio/100
    )