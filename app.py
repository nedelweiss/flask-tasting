from flask import Flask, request

from circle import Circle

app = Flask(__name__)


@app.route('/area', methods=['GET'])
def calculate_area():
    radius = request.args.get("radius")
    return area(radius)

@app.route('/area2', methods=['POST'])
def calculate_area2():
    data = request.get_json(force=True)
    radius = data['radius']
    return area(radius)

def area(radius):
    circle = Circle(float(radius))
    return str(circle.calculate_area())


if __name__ == '__main__':
    app.run()
