from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as file:
        return render_template_string(file.read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
