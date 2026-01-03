import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup Data
us_data = {
    'Symbol': ['XPEV', 'VOO', 'RSP', 'NVDA', 'NIO', 'Li', 'INTC', 'AAPL', 'CRCL'],
    'MV': [612.90, 1039.71, 771.44, 566.55, 77.10, 345.00, 236.28, 542.02, 83.47],
    'Cost': [24.505, 533.48, 179.48, 171.4, 6.719, 31.04, 33.11, 228, 248.28],
    'Price': [20.43, 628.30, 192.86, 188.85, 5.14, 17.25, 39.38, 271.01, 83.47]
}

hk_data = {
    'Symbol': ['Hang Seng TECH', 'SMIC', 'Innovent Bio', 'XIAOMI-W'],
    'MV_HKD': [3432, 37550, 39400, 48336],
    'Sentiment': ['Bullish', 'Bullish', 'Neutral', 'Very Bullish']
}

# 2. Dashboard UI
st.set_page_config(page_title="2026 Portfolio Dashboard", layout="wide")
st.title("🚀 My 2026 Investment Hub")

# Sidebar for News Toggle
st.sidebar.header("Market Intelligence")
show_news = st.sidebar.checkbox("Show 2026 Sentiment Analysis", value=True)

# 3. Main KPIs
col1, col2, col3 = st.columns(3)
col1.metric("US Market Value", "$4,274.72", "-$200.00")
col2.metric("HK Market Value", "128,718 HKD", "-4,300 HKD")
col3.metric("Portfolio Health", "Moderate Risk", "Tech Heavy")

# 4. Charts
st.subheader("Asset Allocation & Performance")
c1, c2 = st.columns(2)

df_us = pd.DataFrame(us_data)
fig_us = px.pie(df_us, values='MV', names='Symbol', title="US Portfolio Weight")
c1.plotly_chart(fig_us)

fig_hk = px.bar(pd.DataFrame(hk_data), x='Symbol', y='MV_HKD', color='Sentiment', title="HK Holdings by Sentiment")
c2.plotly_chart(fig_hk)

# 5. News & Sentiment Module
if show_news:
    st.divider()
    st.subheader("📰 2026 News & Sentiment Feed")
    
    with st.expander("🇨🇳 HK/China Tech Insights (SMIC, Xiaomi)"):
        st.write("""
        * **SMIC (00981):** Sentiment is Bullish for Q1 2026 following a 10% price hike on 12-inch wafers.
        * **Xiaomi (01810):** Strong momentum as EV deliveries hit new milestones in Jan 2026. Target: $53.50 HKD.
        """)
        
    with st.expander("🇺🇸 US Tech & Semi Insights (NVDA, INTC)"):
        st.write("""
        * **NVDA:** AI 'Realization' phase is here. Volatility expected around Q1 earnings, but sentiment remains positive.
        * **INTC:** Recovery play continues. Market watching for 2026 foundry margin improvements.
        """)
