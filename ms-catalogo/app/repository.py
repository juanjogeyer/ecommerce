from app.model import Producto
from app import db
from typing import Optional, List

class ProductoRepository:

    #Agregar producto
    def add_product(self, producto: Producto) -> Producto:
        db.session.add(producto)
        db.session.commit()
        return producto

    #Obtiene todos los productos
    def all(self) -> List[Producto]:
        return db.session.query(Producto).filter(Producto.activado == True).all()

    #Obtiene todos los productos activados
    def find_activo(self, producto_id: int) -> Producto:
        if producto_id is None or producto_id == 0:
            return None
        try:
            return db.session.query(Producto).filter(Producto.id == producto_id, Producto.activado == True).one_or_none()
        except:
            return None