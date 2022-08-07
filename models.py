from sqlalchemy import BLOB
from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

class HydroData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    color=db.Column(db.String(80),nullable=False)
    marker=db.Column(db.Integer)
    size=db.Column(db.Integer,nullable=False)
    pH=db.Column(db.Float,nullable=False)
    Ca=db.Column(db.Integer,nullable=False)
    Mg=db.Column(db.Integer,nullable=False)
    Na=db.Column(db.Integer,nullable=False)
    K=db.Column(db.Float,nullable=False)
    HCO3=db.Column(db.Integer,nullable=False)
    CO3=db.Column(db.Integer,nullable=False)
    Cl=db.Column(db.Integer,nullable=False)
    SO4=db.Column(db.Integer,nullable=False)
    TDS=db.Column(db.Integer,nullable=False)

