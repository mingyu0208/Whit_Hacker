from flask import Flask, render_template, request, send_file
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def list():
    upload_path = "uploads"
    files = []
    for file in os.listdir(upload_path):
        file_path = os.path.join(upload_path, file)
        ctime_datetime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        files.append((file, os.path.getsize(file_path), ctime_datetime))

    return render_template("list.html", files=files)
if __name__ == '__main__':
    app.run(debug=True)