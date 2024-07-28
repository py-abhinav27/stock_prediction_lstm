# Stock Price Prediction Using Keras

This project aims to predict stock prices using a Keras Sequential model, utilizing the 100 Days Exponential Moving Average (EMA) as the default indicator. The project involves data cleaning, preprocessing, model training, and visualization of results. A Streamlit dashboard is provided for user interaction, allowing selection of stock, start date, and end date, and displaying various stock price plots.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Results](#results)
- [Deployment](#deployment)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Stock Price Prediction is a machine learning project that leverages the power of Keras, a deep learning library, to predict future stock prices. The model uses historical stock data to forecast future prices and helps in making informed investment decisions.

## Technologies Used

- **Keras**: For building and training the machine learning model.
- **NumPy**: For numerical operations and data manipulation.
- **Pandas**: For data cleaning and preprocessing.
- **Yahoo Finance**: For fetching historical stock data.
- **Matplotlib**: For plotting graphs and visualizing data.
- **Google Colab**: As an editor for writing and executing code.
- **Streamlit**: For creating an interactive dashboard.
- **Render**: For deploying the project online.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/py-abhinav27/stock_prediction_lstm.git
    ```
2. Navigate to the project directory:
    ```bash
    cd stock_prediction_lstm
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the project in Google Colab or your local editor.
2. Run the `app.py` script to start the Streamlit server:
    ```bash
    streamlit run app.py
    ```
3. Open your browser and navigate to `http://localhost:8501` to access the dashboard.

## Features

- **Stock Data Selection**: Select the stock symbol, start date, and end date.
- **Graphical Analysis**:
  - Closing Price vs 20 EMA
  - Closing Price vs 20 EMA vs 100 EMA
  - Closing Price vs 100 EMA vs 200 EMA
  - Original vs Predicted Price

## Results

The model predicts future stock prices based on historical data and displays the results in an interactive dashboard. Users can compare the predicted prices with actual prices and analyze the performance of the model.

## Deployment

The project is deployed online using Render. You can access the live application [here](https://stock-prediciton-lstm.onrender.com).

## Demo

![Demo](https://imgur.com/a/FI0vSC4)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss improvements, bugs, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact:
- Abhinav Trivedi: [abhinavtrivedi2718@gmail.com](mailto:abhinavtrivedi2718@gmail.com)
- LinkedIn: [Abhinav Trivedi](https://www.linkedin.com/in/abhinav-trivedi-a78834226/)
- GitHub: [py-abhinav27](https://github.com/py-abhinav27)

