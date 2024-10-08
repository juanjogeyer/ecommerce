from app import db
from datetime import datetime

class Compra(db.Model):
    __tablename__ = 'compras'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, nullable=False)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    direccion_envio = db.Column(db.String(255), nullable=False)

    producto = db.relationship('Producto', backref='compras')