from app import db

class Pago(db.Model):
    __tablename__ = 'pagos'

    id: int = db.Column(db.Integer, primary_key=True)
    producto_id: int = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    precio: float = db.Column(db.Float, nullable=False)
    medio_pago: str = db.Column(db.String(50), nullable=False)

    producto = db.relationship('Producto', backref='pagos')