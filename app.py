import streamlit as st
import pandas as pd
import plotly.express as px
import finnhub
from datetime import datetime, timedelta

# Initialize Finnhub (Replace with your actual key)
FINNHUB_KEY = 'd5c9ko9r01qsbmgjdvfgd5c9ko9r01qsbmgjdvg0'
finnhub_client = finnhub.Client(api_key=FINNHUB_KEY)

st.set_page_config(page_title="Investment Terminal 2026", layout="wide")
st.title("📟 Global Portfolio Terminal")

# Sidebar for global settings
st.sidebar.header("Global Controls")
currency_mode = st.sidebar.selectbox("Base Currency", ["HKD", "USD"])

# Define Tabs
tab_perf, tab_alloc, tab_hold, tab_sent, tab_plan = st.tabs([
    "📈 Performance", "🍕 Allocation", "📋 Holdings", "🎭 Sentiment", "📝 2026 Plan"
])

# --- TAB 1: PERFORMANCE ---
with tab_perf:
    st.subheader("Equity Curve & P/L Trends")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Value", "$162,783 HKD", "+1.36%")
    col2.metric("2025 Total Return", "15.79%", "vs HSI 27.8%")
    col3.metric("Daily Alpha", "0.45%", "Bullish")
    
    # Placeholder for a performance line chart
    chart_data = pd.DataFrame({'Date': pd.date_range('2025-01-01', periods=12, freq='M'), 
                               'Portfolio': [100, 105, 102, 110, 108, 115, 120, 118, 125, 122, 130, 135]})
    fig_perf = px.line(chart_data, x='Date', y='Portfolio', title="Portfolio Growth vs. Time")
    st.plotly_chart(fig_perf, use_container_width=True)

# --- TAB 2: ALLOCATION ---
with tab_alloc:
    st.subheader("Asset & Geographic Distribution")
    c1, c2 = st.columns(2)
    
    # Geographic Data
    geo_data = {'Region': ['Hong Kong', 'United States', 'Cash'], 'Value': [128718, 33342, 723]}
    fig_geo = px.pie(geo_data, values='Value', names='Region', hole=0.5, title="Geographic Exposure")
    c1.plotly_chart(fig_geo)
    
    # Sector Data
    sec_data = {'Sector': ['EV/Auto', 'Semiconductors', 'Index ETF', 'Tech'], 'Value': [40, 30, 20, 10]}
    fig_sec = px.bar(sec_data, x='Sector', y='Value', title="Sector Concentration (%)")
    c2.plotly_chart(fig_sec)

# --- TAB 3: HOLDINGS ---
with tab_hold:
    st.subheader("Detailed Position Registry")
    # Simplified dataframe from your previous input
    holdings_df = pd.DataFrame([
        {"Symbol": "XIAOMI-W", "Qty": 1200, "Cost": 32.00, "Price": 40.28, "P/L %": "+25.8%"},
        {"Symbol": "SMIC", "Qty": 500, "Cost": 79.35, "Price": 75.10, "P/L %": "-5.3%"},
        {"Symbol": "NVDA", "Qty": 3, "Cost": 171.4, "Price": 188.85, "P/L %": "+10.1%"},
        {"Symbol": "XPEV", "Qty": 30, "Cost": 24.50, "Price": 20.43, "P/L %": "-16.6%"}
    ])
    st.table(holdings_df)

# --- TAB 4: SENTIMENT (Finnhub Integration) ---
with tab_sent:
    st.subheader("Live Market Sentiment Feed")
    ticker = st.text_input("Enter Ticker to Analyze (e.g., AAPL or 01810.HK)", "01810.HK")
    
    if st.button("Fetch Intelligence"):
        # Fetch News
        clean_ticker = ticker.split('.')[0] if '.' in ticker else ticker
        news = finnhub_client.company_news(clean_ticker, _from='2025-12-01', to='2026-01-03')
        
        for article in news[:3]:
            with st.chat_message("assistant"):
                st.write(f"**{article['headline']}**")
                st.caption(f"Source: {article['source']} | Sentiment: Real-time Analysis Required")
                st.write(article['summary'][:150] + "...")

# --- TAB 5: 2026 PLAN ---
with tab_plan:
    st.subheader("Strategic Roadmap for 2026")
    st.info("🎯 **Goal:** Rebalance to 15% Cash and 20% Non-Tech to lower volatility.")
    
    with st.expander("Q1 Actions"):
        st.write("- Trim **Xiaomi** if it touches $50 HKD.")
        st.write("- Average down on **SMIC** if it dips below $70 HKD.")
    
    with st.expander("Risk Management"):
        st.warning("Concentration in Chinese EVs is high. Stop-loss set at -20% for XPEV.")
