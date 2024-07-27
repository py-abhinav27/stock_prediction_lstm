import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt
import datetime

model = load_model(r'C:\Users\DELL\Desktop\Stock Price Prediction\Stock Predictions LSTM.keras')

st.set_page_config(
    page_title="Stock Price Predicition LSTM",
    page_icon="📈",
    initial_sidebar_state="expanded"
)
st.title('Stock Market Predictor')

with st.sidebar:
    a = st.sidebar.text('Thanks for Visiting!')
    b = st.sidebar.link_button('Check Out on Github','https://github.com/py-abhinav27')
    c = st.sidebar.text('Made with ❤ by Abhinav Trivedi')

stock = st.text_input('Enter Stock Symnbol', 'META')
start_date = st.date_input('Enter Starting Date',datetime.date(2002,11,27))
end_date = st.date_input('Enter Ending Date',min_value=datetime.date(2002,1,1))


data = yf.download(stock, start_date, end_date)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0: int(len(data) * 0.80)])
data_test = pd.DataFrame(data.Close[int(len(data) * 0.80): len(data)])

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scale = scaler.fit_transform(data_test)

st.subheader('Price vs MA20')
ma_20_days = data.Close.rolling(20).mean()
fig1 = plt.figure(figsize=(8, 6))
plt.plot(ma_20_days, 'r', label = '20 Days EMA')
plt.plot(data.Close, 'g', label = 'Closing')
plt.legend()
plt.show()
st.pyplot(fig1)

st.subheader('Price vs MA20 vs MA100')
ma_100_days = data.Close.rolling(100).mean()
fig2 = plt.figure(figsize=(8, 6))
plt.plot(ma_20_days, 'r', label = '20 Days EMA')
plt.plot(ma_100_days, 'b', label = '100 Days EMA')
plt.plot(data.Close, 'g', label = 'Closing Price')
plt.legend()
plt.show()
st.pyplot(fig2)

st.subheader('Price vs MA100 vs MA200')
ma_200_days = data.Close.rolling(200).mean()
fig3 = plt.figure(figsize=(8, 6))
plt.plot(ma_100_days, 'r', label = '100 Days EMA')
plt.plot(ma_200_days, 'b', label = '200 Days EMA')
plt.plot(data.Close, 'g', label = 'Closing Price')
plt.legend()
plt.show()
st.pyplot(fig3)

x = []
y = []

for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i - 100:i])
    y.append(data_test_scale[i, 0])

x, y = np.array(x), np.array(y)

predict = model.predict(x)

scale = 1 / scaler.scale_

predict = predict * scale
y = y * scale

st.subheader('Original Price vs Predicted Price')
fig4 = plt.figure(figsize=(8, 6))
plt.plot(predict, 'r', label='Original Price')
plt.plot(y, 'g', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig4)
