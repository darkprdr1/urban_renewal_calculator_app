# 🏙️ 都市更新權利變換試算模型

本專案提供防災型都市更新模擬工具，協助使用者進行容積計算、成本估算與權利分配試算。

👉 線上版本：[點我啟動](https://urbanrenewalcalculatorapp-vpupa84rtvl6hgtxv2pili.streamlit.app)

## ✅ 使用方式

### 本地執行

```bash
git clone https://github.com/你的帳號/urban_renewal_calculator_app.git
cd urban_renewal_calculator_app
pip install -r requirements.txt
streamlit run app.py
```

## 🧱 模組結構

- `app.py`：主介面與排版
- `modules/`：功能模組（容積、費用、分配、敏感度）
- `requirements.txt`：必要套件清單

## 📦 安裝需求

```
streamlit
pandas
plotly
```

## 📍 注意事項

此模型為試算用途，並未套用實際建築容積審查或財務利潤模型。輸入數值應視個案調整。
