from flask import Flask, jsonify, request
app = Flask(__name__)

from sigma import Sigma, IFD, DG
from construct import Container

camera = Sigma()
# camera = PTPy(extension=sigma.Sigma, idVendor=0x1003, idProduct=0xc432)

@app.route('/')
def home():
    return 'hoge'

@app.route('/api/open_session')
def open_session():
    response = camera.open_session()
    return response

@app.route('/api/close_session')
def close_session():
    response = camera.close_session()
    return response

@app.route('/api/config')
def config():
    response = camera.config_api()
    return response.Data

@app.route('/api/cam_data_group1_dummy', methods=['GET', 'POST'])
def cam_data_group1_dummy():
    if request.method == 'GET':
        dg = camera.get_cam_data_group1_dummy()
        return jsonify(dg.items())
    elif request.method == 'POST':
        dg = DG(DG.data_group1_endian, Container(**request.json))
        result = camera.set_cam_data_group1_dummy(dg)
        return result
    else:
        return ''

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=10080)
