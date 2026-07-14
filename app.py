from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lab 8 - Cloud Computing - Thông Lương</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

            body {
                margin: 0;
                padding: 0;
                /* Nền gradient chuyển màu liên tục */
                background: linear-gradient(45deg, #0f0c29, #302b63, #24243e, #0f0c29);
                background-size: 400% 400%;
                animation: gradientBG 10s ease infinite;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Orbitron', sans-serif;
                color: #fff;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 40px 60px;
                border-radius: 15px;
                /* Viền phát sáng neon xanh cyan */
                box-shadow: 0 0 20px #00ffff, inset 0 0 20px #00ffff;
                border: 2px solid #00ffff;
                text-align: center;
                position: relative;
                overflow: hidden;
            }

            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                color: #ff00ff;
                /* Hiệu ứng chữ chớp nháy neon hồng */
                text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
                animation: pulsate 1.5s infinite alternate;
            }

            h2 {
                font-size: 1.5em;
                color: #00ff00;
                text-shadow: 0 0 8px #00ff00;
                margin-bottom: 30px;
            }

            .info {
                font-size: 1.3em;
                color: #00ffff;
                margin: 15px 0;
                letter-spacing: 2px;
            }

            .highlight {
                color: #ffea00;
                text-shadow: 0 0 8px #ffea00;
                font-weight: bold;
            }

            hr {
                border: 1px solid #00ffff;
                box-shadow: 0 0 10px #00ffff;
                margin: 25px 0;
            }

            .footer {
                font-size: 1em;
                color: #ff0055;
                text-shadow: 0 0 8px #ff0055;
                margin-top: 20px;
            }

            @keyframes pulsate {
                100% { text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff, 0 0 60px #ff00ff; }
                0% { text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CLOUD COMPUTING</h1>
            <h2>LAB 8: JENKINS & DOCKER CI/CD PIPELINE</h2>
            <hr>
            <p class="info">Sinh viên thực hiện: <span class="highlight">Lương Hoàng Thông</span></p>
            <p class="info">Mã số sinh viên: <span class="highlight">23DH113430</span></p>
            <hr>
            <p class="footer">🚀 Trạng thái: Hệ thống tự động triển khai thành công trên AWS! 🚀</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)