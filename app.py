import streamlit as st
import MetaTrader5 as mt5

# ==========================================
# 1. APKI LIVE LOGIN DETAILS
# ==========================================
ACCOUNT_ID = 260820558
PASSWORD = "Yall@1234567"
SERVER = "Exness-MT5Trial15"

# ==========================================
# 2. TARGET SETTINGS ($10k Profit Target)
# ==========================================
START_BAL = 100000.0
PROFIT_GOAL = 10000.0
FINAL_TARGET = START_BAL + PROFIT_GOAL # $110,000

# ==========================================
# 3. AUTO-CLOSE FUNCTION (Full Trading Access)
# ==========================================
def close_all_positions():
    """Target hit hone par sari trades foran band karne ke liye"""
    positions = mt5.positions_get()
    if positions:
        for p in positions:
            tick = mt5.symbol_info_tick(p.symbol)
            # Opposite order logic to close
            order_type = mt5.ORDER_TYPE_SELL if p.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if p.type == mt5.POSITION_TYPE_BUY else tick.ask
            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": p.ticket,
                "symbol": p.symbol,
                "volume": p.volume,
                "type": order_type,
                "price": price,
                "magic": 123456,
                "comment": "Jarvis Target Reached",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            result = mt5.order_send(request)
            if result.retcode == mt5.TRADE_RETCODE_DONE:
                st.write(f"✅ Closed: {p.symbol} (Ticket: {p.ticket})")

# ==========================================
# 4. STREAMLIT DASHBOARD & MONITORING
# ==========================================
st.set_page_config(page_title="Jarvis Pro Terminal", layout="centered")
st.title("🤖 Jarvis AI Trading Bot")

# Connection initialize karein
if not mt5.initialize(login=ACCOUNT_ID, password=PASSWORD, server=SERVER):
    st.error(f"❌ MT5 Connection Failed! Error: {mt5.last_error()}")
else:
    acc_info = mt5.account_info()
    if acc_info:
        current_balance = acc_info.balance
        profit_loss = current_balance - START_BAL
        
        # UI Metrics
        col1, col2 = st.columns(2)
        col1.metric("Current Balance", f"${current_balance:,.2f}")
        col2.metric("Total Profit/Loss", f"${profit_loss:,.2f}", delta=f"${profit_loss}")

        # Progress bar toward $110,000
        progress = min(max(profit_loss / PROFIT_GOAL, 0.0), 1.0)
        st.progress(progress)
        st.write(f"🎯 Target Progress: {progress*100:.1f}%")

        # --- AUTO-STOP LOGIC ---
        if current_balance >= FINAL_TARGET:
            st.balloons()
            st.success(f"🏆 TARGET REACHED! Account Balance: ${current_balance}")
            st.warning("🔄 Closing all positions and stopping Jarvis...")
            close_all_positions()
            mt5.shutdown()
            st.stop()
        else:
            st.info("🛰️ Jarvis is scanning the market. Auto-stop active at $110,000.")

# Yahan se niche aap apni SMC / Jarvis strategy ka logic paste kar sakte hain
