from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Pre teba ❤️</title>
        <style>
            body { 
                background-color: #ffe6e6;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 10%;
            }
            .heart { font-size: 150px; color: red; }
        </style>
    </head>
    <body>
        <div class="heart">❤️</div>
        <h1>Len pre teba ❤️</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

