from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
def detect_phishing(url):
    url = url.lower() 
    
    keywords = ['login', 'verify', 'update', 'secure', 'banking', 'account', 'amtso']
    for word in keywords:
        if word in url and ("google.com" not in url and "microsoft.com" not in url):
            return f"Suspicious (Keyword: {word})"


    if "demo_site" in url or "login.html" in url:
        return "⚠️ DANGER: Locally Hosted Phishing Simulation"
    
    if len(url) > 75:
        return "Warning (URL is unusually long)"

    if url.count('.') > 3:
        return "Dangerous (Too many subdomains)"

    if not url.startswith("https"):
        return "Warning (Insecure Connection)"

    if "amtso" in url:
        return "Detected: AMTSO Phishing Test Page"

    return "Safe"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url', '')
    result = detect_phishing(url)
    return jsonify({"status": result})

if __name__ == '__main__':
    app.run(debug=True)