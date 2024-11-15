from flask import Flask, render_template, send_from_directory
from dash import Dash
import dash_bootstrap_components as dbc
from dashboard.dashboard import create_dashboard

# Initialize Flask app
server = Flask(__name__)

# Initialize Dash app
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/dashboard/',
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css",
        "/static/styles.css"
    ],
    external_scripts=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
    ],
    title="NISR-Youth Unemployment"
)

# Create dashboard layout and callbacks
create_dashboard(app)

# Define a route for the home page
@server.route('/')
def home():
    return render_template('index.html')

# Serve static files
@server.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

# Run the server (only locally, not on PythonAnywhere)
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
