from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!doctype html>
    <html lang="fa">
    <head>
        <meta charset="utf-8">
        <title>TGStream</title>
        <style>
            body {
                font-family: sans-serif;
                background: #0f172a;
                color: #e5e7eb;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: #111827;
                padding: 2rem 3rem;
                border-radius: 1rem;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
                max-width: 600px;
                text-align: center;
            }
            h1 {
                margin-top: 0;
                color: #38bdf8;
            }
            a {
                color: #22c55e;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            code {
                background: #020617;
                padding: 0.2rem 0.4rem;
                border-radius: 0.25rem;
                font-size: 0.9rem;
            }
            .domain {
                margin-top: 1rem;
                font-size: 0.9rem;
                color: #9ca3af;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>TGStream – Online</h1>
            <p>این یک وب‌سایت ساده است که با <code>Flask</code> روی سرور شما بالا آمده.</p>
            <p class="domain">
                دامنه تنظیم‌شده:<br>
                <strong>https://tgstream.apps.apply.build</strong>
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # برای توسعه لوکال
    app.run(host="0.0.0.0", port=443)
