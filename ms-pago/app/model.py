from app import db

class Pago(db.Model):
    __tablename__ = 'pagos'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    medio_pago = db.Column(db.String(50), nullable=False)

    producto = db.relationship('Producto', backref='pagos')