from fastapi import FastAPI
from growwapi import GrowwAPI
import pyotp
import os
from dotenv import load_dotenv
import time
load_dotenv()


api_key = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

totp = pyotp.TOTP(API_SECRET).now()

access_token = GrowwAPI.get_access_token(
    api_key=api_key,
    totp=totp
)

groww = GrowwAPI(access_token)
app=FastAPI()

@app.get('/')
def home():
    return {"message":"hello"}


@app.get('/twenty_min')
def fetch_twenty_min():
    # you can give time programatically.
    end_time_in_millis = int(time.time() * 1000) # epoch time in milliseconds
    start_time_in_millis = end_time_in_millis - (24 * 60 * 60 * 1000) # last 24 hours
 
# OR
 
# you can give start time and end time in yyyy-MM-dd HH:mm:ss format.
    end_time = "2026-01-26 14:00:00"
    start_time = "2025-12-27 10:00:00"
 
    historical_data_response = groww.get_historical_candle_data(
    trading_symbol="RELIANCE",
    exchange=groww.EXCHANGE_NSE,
    segment=groww.SEGMENT_CASH,
    start_time=start_time,
    end_time=end_time,
    interval_in_minutes=20 # Optional: Interval in minutes for the candle data
)
    return historical_data_response


w

