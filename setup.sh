
python3 -m venv venv
cd ./venv
source bin/activate

# pip install --upgrade pip

pip install streamlit yfinance pandas plotly watchdog

streamlit run ../stock_app.py

