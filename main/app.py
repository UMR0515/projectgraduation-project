from flask import Flask, request, jsonify, send_file, render_template

app = Flask(__name__, static_folder=".", template_folder=".")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_script", methods=["POST"])
def generate_script():
    data = request.json
    operation = data.get("operation")

    # 根據操作生成 Python 腳本
    if operation == "clear_first_row":
        script = """import pandas as pd
df = pd.read_excel("input.xlsx")
df.iloc[0] = None  # 清空第一行
df.to_excel("output.xlsx", index=False)"""
    elif operation == "delete_column":
        script = """import pandas as pd
df = pd.read_excel("input.xlsx")
df.drop(df.columns[1], axis=1, inplace=True)  # 刪除第二欄
df.to_excel("output.xlsx", index=False)"""
    else:
        return jsonify({"error": "無效的操作"})

    return jsonify({"script": script})

@app.route("/download_script")
def download_script():
    # 假設生成的腳本保存在當前目錄下
    script_path = "generated_script.py"
    with open(script_path, "w") as f:
        f.write("""import pandas as pd
df = pd.read_excel("input.xlsx")
df.to_excel("output.xlsx", index=False)""")
    return send_file(script_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)