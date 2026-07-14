from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Giao diện HTML đơn giản hiển thị thông tin sinh viên và môn học
    return """
    <html>
        <head>
            <title>Lab 8 - Cloud Computing</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    margin-top: 100px; 
                    background-color: #f4f6f9;
                    color: #333;
                }
                .container { 
                    display: inline-block; 
                    padding: 30px; 
                    background: white; 
                    border-radius: 10px; 
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.1); 
                }
                h1 { color: #0056b3; }
                h2 { color: #28a745; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>MÔN HỌC: CLOUD COMPUTING</h1>
                <h2>LAB 8: TRIỂN KHAI CI/CD PIPELINE VỚI JENKINS VÀ DOCKER</h2>
                <hr>
                <p><b>Sinh viên thực hiện:</b> Trần Phan Cảnh Phúc</p>
                <p><b>Mã số sinh viên (MSSV):</b> 23DH112758</p>
                <hr>
                <p style="color: #666; font-size: 14px;"><i>Trạng thái: Pipeline hoạt động hoàn toàn tự động trên AWS EC2!</i></p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)