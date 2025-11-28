from flask import Flask

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
            .heart {
                font-size: 150px;
                color: red;
            }
        </style>
    </head>
    <body>
        <div class="heart">❤️</div>
        <h1>Láska chýbaš mi ❤️</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
