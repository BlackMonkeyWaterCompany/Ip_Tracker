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

