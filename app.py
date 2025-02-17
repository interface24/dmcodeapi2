from flask import Flask, request, send_file
from pystrich.datamatrix import DataMatrixEncoder
from PIL import Image
import io

app = Flask(__name__)


@app.route('/generate', methods=['GET'])
def generate_datamatrix():
    data = request.args.get('data')
    if not data:
        return {"error": "Missing 'data' parameter"}, 400

    encoder = DataMatrixEncoder(data)
    img_data = encoder.get_imagedata()  # Holt das Bild als Rohbytes

    # Konvertiere das Byte-Array in ein PIL-Image
    img = Image.open(io.BytesIO(img_data))

    # Speichere das Bild in einem BytesIO-Objekt
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)