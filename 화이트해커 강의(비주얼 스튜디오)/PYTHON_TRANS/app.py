from flask import Flask, render_template, request, send_file
import googletrans
import os
import openpyxl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join("uploads", file.filename))

    workbook = openpyxl.load_workbook(os.path.join("uploads", file.filename))
    sheet = workbook.active

    translator = googletrans.Translator()

    for row in sheet.iter_rows():
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text
            cell.value = translated_text

    workbook.save("result.xlsx")

    return render_template('result.html', file_name = file.filename)

@app.route('/download_report')
def download_report():
    return send_file('result.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)