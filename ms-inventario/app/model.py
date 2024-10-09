from sqlalchemy import CheckConstraint
from app import db

class Stock(db.Model):
    __tablename__ = 'stock'

    id: int = db.Column(db.Integer, primary_key=True)
    producto_id: int = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    fecha_transaccion = db.Column(db.DateTime, nullable=False)
    cantidad: float = db.Column(db.Float, nullable=False)
    entrada_salida: int = db.Column(db.Integer, CheckConstraint('entrada_salida IN (1, 2)'), nullable=False)  # 1: entrada, 2: salida

    producto = db.relationship('Producto', backref='stock')