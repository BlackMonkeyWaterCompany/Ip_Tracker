import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def track_ip():
    user_ip = request.remote_addr
    ip_info = requests.get(f"https://ipinfo.io/{user_ip}/json").json()
    
    return render_template("index.html", ip=user_ip, location=ip_info.get("city", "Unknown"), country=ip_info.get("country", "Unknown"), isp=ip_info.get("org", "Unknown"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def track_ip():
    # Get the IP address of the user
    user_ip = request.remote_addr
    
    # Optionally, log the IP address to a file or database (example: logging to console)
    print(f"User IP: {user_ip}")
    
    # Get information about the IP address using ipinfo.io
    ip_info = requests.get(f"https://ipinfo.io/{user_ip}/json").json()

    return f"Your IP is {user_ip}. Location: {ip_info.get('city', 'Unknown')}, {ip_info.get('country', 'Unknown')}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

