from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Define el directorio donde se guardarán los archivos subidos
UPLOAD_FOLDER = './archivos_subidos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta para renderizar el formulario HTML
@app.route('/')
def index():
    return render_template('form.html')  # Renderiza el archivo HTML

# Ruta para procesar el archivo subido
@app.route('/subir_archivo', methods=['POST'])
def subir_archivo():
    if 'archivoAAC' not in request.files:
        return "No se seleccionó ningún archivo"
    
    archivo = request.files['archivoAAC']

    if archivo.filename == '':
        return "No se seleccionó un nombre de archivo válido"

    # Verifica si el archivo es AAC y guárdalo
    if archivo and archivo.filename.endswith('.aac'):
        ruta_archivo = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
        archivo.save(ruta_archivo)  # Guarda el archivo en la carpeta UPLOAD_FOLDER
        return f"Archivo {archivo.filename} subido exitosamente"
    else:
        return "Solo se permiten archivos AAC."

# Ejecuta la aplicación
if __name__ == '__main__':
    # Crea la carpeta para subir archivos si no existe
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)
