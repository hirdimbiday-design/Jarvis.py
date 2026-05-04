import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="Jarvis Dashboard", layout="wide")
st.title("🤖 Jarvis Trading Dashboard")

# Sidebar for Navigation and Settings
st.sidebar.header("Control Panel")
page = st.sidebar.radio("Go to", ["Live Status", "Trading Performance"])
pair = st.sidebar.selectbox("Select Asset", ["XAUUSD", "BTCUSD", "ETHUSD"])

if page == "Live Status":
    st.subheader(f"📊 Market Monitoring: {pair}")
    
    # Live Metrics Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Status", "Connected", "Live")
    col2.metric("Active Pair", pair)
    col3.metric("Strategy", "Price Action / SMC")

    st.info(f"🔍 Jarvis is searching for Price Action patterns on {pair}...")

    # TradingView Chart Section
    st.write("---")
    st.subheader(f"📈 Live {pair} Chart")
    
    # TradingView Widget Logic
    symbol = f"OANDA:{pair}" if pair == "XAUUSD" else f"BINANCE:{pair}P"
    
    tradingview_html = f"""
    <div class="tradingview-widget-container" style="height: 500px;">
        <div id="tradingview_chart"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({{
            "autosize": true,
            "symbol": "{symbol}",
            "interval": "15",
            "timezone": "Etc/UTC",
            "theme": "dark",
            "style": "1",
            "locale": "en",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "hide_side_toolbar": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_chart"
        }});
        </script>
    </div>
    """
    components.html(tradingview_html, height=550)

else:
    st.subheader("📈 Trading Performance")
    st.write("Logs and analytics will appear here once the bot starts trading.")
    st.info("Performance tracking is currently in standby mode.")

  
