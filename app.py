from flask import Flask, render_template, request
from zipfile import ZipFile
import os

app = Flask(__name__)

def AlphaFoldXploR_read(zfile):
    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".json"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista1 = fz.extract(zip_info, "archivos_json")

    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".pdb"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista2 = fz.extract(zip_info, "archivos_pdb")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            zfile = uploaded_file.filename
            uploaded_file.save(zfile)

            # Llamada a la función AlphaFoldXploR_read
            AlphaFoldXploR_read(zfile)

            return "Archivo cargado y procesado con éxito."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
