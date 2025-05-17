from flask import Flask, request, send_file
from circle import Circle
from PIL import Image
import io

app = Flask(__name__)

@app.route('/area', methods=['GET'])
def calculate_area():
    radius = request.args.get("radius")
    return area(radius)

@app.post('/area2')
def calculate_area2():
    data = request.get_json(force=True)
    radius = data['radius']
    return area(radius)

@app.route('/upload', methods=['POST'])
def upload_img():
    file_storage = request.files['image']
    colorful_img_bytes = io.BytesIO(file_storage.read())
    opened_colorful_img = Image.open(colorful_img_bytes)
    gray_img = opened_colorful_img.convert('L')
    gray_img_format = opened_colorful_img.format
    img_name = 'gray_' + str(file_storage.filename)
    # gray_img.save(img_name) # save locally
    # gray_img.show()

    gray_img_bytes = io.BytesIO()
    gray_img.save(gray_img_bytes, format=gray_img_format)
    gray_img_bytes.seek(0)

    # bytes_io = io.BytesIO(gray_img.tobytes()) # it corrupts metadata
    build_img_format = 'image/' + gray_img_format.lower()
    return send_file(gray_img_bytes, mimetype=build_img_format, as_attachment=True, download_name=img_name)

def area(radius):
    circle = Circle(float(radius))
    return str(circle.calculate_area())

if __name__ == '__main__':
    app.run()
