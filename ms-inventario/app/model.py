from app import db

class Inventario(db.Model):
    __tablename__ = 'inventarios'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    fecha_transaccion = db.Column(db.DateTime, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    entrada_salida = db.Column(db.Integer, nullable=False)  # 1: entrada, 2: salida

    producto = db.relationship('Producto', backref='inventarios')