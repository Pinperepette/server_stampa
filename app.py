#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cups

app = Flask(__name__)

# Funzione per stampare il documento
def print_document(file_path, printer_name):
    conn = cups.Connection()
    printers = conn.getPrinters()
    
    if printer_name in printers:
        conn.printFile(printer_name, file_path, "Stampa da Python", {})
        print("Documento inviato alla stampante con successo.")
        return True
    else:
        print("Stampante non trovata. Assicurati di specificare un nome di stampante valido.")
        return False

# Pagina principale per caricare il documento
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Utilizza secure_filename per ottenere un nome di file sicuro
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join("uploads", filename)
            uploaded_file.save(file_path)
            printer_name = request.form['printer']
            if print_document(file_path, printer_name):
                os.remove(file_path)
                return "Documento stampato con successo!"
            else:
                return "Errore durante la stampa."
    return render_template('index.html', printers=cups.Connection().getPrinters())

if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True, host='0.0.0.0', port=5050)
