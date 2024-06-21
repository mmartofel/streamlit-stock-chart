import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objs as go

# Set default stock symbol
default_stock_symbol = "NVDA"

# Title of the app
st.title("Visualizing Stock Data")

# Input field for the user to enter a stock symbol
stock_symbol = st.text_input("Enter stock symbol", default_stock_symbol).upper()

# Fetch stock data
stock_data = yf.Ticker(stock_symbol)

# Get stock info and history
stock_info = stock_data.info
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365)
stock_history = stock_data.history(start=start_date, end=end_date)

# Display company name and current stock price in bold
st.markdown(f"**Company Name:** {stock_info['longName']}")
st.markdown(f"**Current Price:** ${stock_info['currentPrice']}")

# Chart showing closing prices over the past year
st.subheader("Closing Prices Over the Past Year")
fig_close = go.Figure()
fig_close.add_trace(go.Scatter(x=stock_history.index, y=stock_history['Close'], mode='lines', name='Close'))
fig_close.update_layout(title='Closing Prices', xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(fig_close)

# Chart showing the volume of stock trades over the past year
st.subheader("Volume of Stock Trades Over the Past Year")
fig_volume = go.Figure()
fig_volume.add_trace(go.Bar(x=stock_history.index, y=stock_history['Volume'], name='Volume'))
fig_volume.update_layout(title='Volume of Trades', xaxis_title='Date', yaxis_title='Volume')
st.plotly_chart(fig_volume)

# Calculate moving averages
stock_history['20D MA'] = stock_history['Close'].rolling(window=20).mean()
stock_history['50D MA'] = stock_history['Close'].rolling(window=50).mean()

# Line chart showing closing price, 20 day moving average, and 50 day moving average
st.subheader("Closing Price with 20 and 50 Day Moving Averages")
fig_ma = go.Figure()
fig_ma.add_trace(go.Scatter(x=stock_history.index, y=stock_history['Close'], mode='lines', name='Close'))
fig_ma.add_trace(go.Scatter(x=stock_history.index, y=stock_history['20D MA'], mode='lines', name='20D MA'))
fig_ma.add_trace(go.Scatter(x=stock_history.index, y=stock_history['50D MA'], mode='lines', name='50D MA'))
fig_ma.update_layout(title='Closing Price with 20 and 50 Day Moving Averages', xaxis_title='Date', yaxis_title='Price')
st.plotly_chart(fig_ma)


