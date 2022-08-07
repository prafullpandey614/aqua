import imp
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from numpy import imag
from models import HydroData,Img
import os
from g import graph
from flask import request,Response
from werkzeug.utils import secure_filename 

from db import db_init,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data2.db'

db_init(app)

imag_file=None

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/upload', methods=["GET",'POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


@app.route('/<int:id>')
def get_img(id):
    global imag_file
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404
     
    imag_file=f"http://127.0.0.1:5000/2"
    
    return Response(img.img, mimetype=img.mimetype)


def uploadingData():
   pass

@app.route('/data')
def get_data():
    # uploadingData()
    graph()
    datas=HydroData.query.all()
    output=[]
    imag1="http://127.0.0.1:5000/1"
    imag2="http://127.0.0.1:5000/2",
    imag3="http://127.0.0.1:5000/3"
    imageout={imag1,imag2,imag3}
    for data in datas:
        hydro_info={'id':data.id,
                    'color':data.color,
                    'marker':data.marker,
                    'size':data.size,
                    'pH':data.pH,
                    'Ca':data.Ca,
                    'Mg':data.Mg,
                    'Na':data.Na,
                    'K':data.K,
                    'HCO3':data.HCO3,
                    'CO3':data.CO3,
                    'Cl':data.Cl,
                    'SO4':data.SO4,
                    'TDS':data.TDS}
        output.append(hydro_info)
    output.append(imag1)
    output.append(imag2)
    output.append(imag3)
    return {"HydroChemical Data":output}