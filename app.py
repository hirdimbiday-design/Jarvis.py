import streamlit as st

st.set_page_config(page_title="Jarvis Dashboard", layout="wide")
st.title("🤖 Jarvis Trading Dashboard")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Live Status", "Performance"])

if page == "Live Status":
    st.subheader("Market Monitoring")
    col1, col2 = st.columns(2)
    col1.metric("Status", "Connected", "Running")
    col2.metric("Active Pairs", "XAUUSD, BTCUSD, ETHUSD")
    st.info("Searching for Price Action patterns...")
else:
    st.subheader("Trading Performance")
    st.write("Logs and analytics will appear here.")
  
