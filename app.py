import os
from flask import Flask, render_template, request
from flask_cors import CORS
import whisper  # AI
# librerias para crear el audio recibido en el directorio ./audios/
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
model = whisper.load_model("base")


def procesarAudio(request):
    audio = request.files['audio_file']
    filename = secure_filename(audio.filename)
    audio.save(os.path.join(app.config['/audios'], filename))
    result = model.transcribe('./audios/' + filename)
    return result['text']


app = Flask(__name__)
app.config['/audios'] = './audios'
cors = CORS(app)
# app.config['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
# app.config['CORS_HEADERS'] = '*'

@app.route('/transcribe', methods=['POST', 'GET'])
def transcribe():
    if request.method == 'OPTIONS':
        print('HUBO UNA PETICION OPTIONS!!!!')
    elif request.method == 'POST':
        print(request)
        print(request.files['audio_file'])
        transcribeText = procesarAudio(request)
        print(transcribeText)
        return transcribeText
    # return render_template('index.html')
    return f"HOLA, HICISTE UN {request.method}"

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')


# if __name__ == '__name__':
app.run(port=3000, debug=True)
