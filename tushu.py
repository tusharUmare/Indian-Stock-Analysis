import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Title
st.title("📈 Stock Price Viewer")
st.markdown("Visualize closing prices of stocks from a CSV dataset")

# Load data
df = pd.read_csv("IFA.csv")
df = df.drop("Unnamed: 0", axis=1)
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar: Stock selection
stock_list = df["Symbol"].unique()
selected_stock = st.sidebar.selectbox("Choose a Stock Symbol:", stock_list)

# Filter data
stk = df[df["Symbol"] == selected_stock]

# Plotting
st.subheader(f"📊 Closing Prices for {selected_stock}")
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(x=stk["Date"], y=stk["Close"], ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
plt.xticks(rotation=45)
st.pyplot(fig)
