import os
import dash

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

app = dash.Dash(__name__, suppress_callback_exceptions=True)