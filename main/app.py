from flask import Flask, request, jsonify, send_file, render_template
import json
import os

app = Flask(__name__)

# 從 data.json 讀取腳本模板
with open("C:\\Users\\Acer\\Desktop\\py入門\\專案\\EXCEL\\main\\data.json", "r", encoding="utf-8") as f:
    SCRIPT_TEMPLATES = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_script", methods=["POST"])
def generate_script():
    data = request.json
    operation = data.get("operation")

    if operation not in SCRIPT_TEMPLATES:
        return jsonify({"error": "Invalid operation"}), 400

    script_content = SCRIPT_TEMPLATES[operation]
    
    # 把程式碼寫入檔案，提供下載
    script_filename = "generated_script.py"
    with open(script_filename, "w", encoding="utf-8") as f:
        f.write(script_content)

    return jsonify({"script": script_content, "download_url": "/download_script"})

@app.route("/download_script", methods=["GET"])
def download_script():
    return send_file("generated_script.py", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
