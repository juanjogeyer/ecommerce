from app.model import Producto
from app import db
from typing import Optional, List

class ProductoRepository:
    
    def save(self, producto: Producto) -> Producto:
        """Guarda un nuevo producto en la base de datos."""
        db.session.add(producto)
        db.session.commit()
        return producto

    def find(self, producto_id: int) -> Optional[Producto]:
        """Busca un producto por su ID."""
        return db.session.query(Producto).filter(Producto.id == producto_id, Producto.activado == True).one_or_none()

    def update(self, producto: Producto) -> Optional[Producto]:
        """Actualiza los datos de un producto existente."""
        existing_producto = self.find(producto.id)
        existing_producto.nombre = producto.nombre
        existing_producto.precio = producto.precio
        existing_producto.activado = producto.activado
        db.session.commit()
        return existing_producto

    def delete(self, producto_id: int) -> bool:
        """Elimina (desactiva) un producto marcándolo como inactivo."""
        producto = self.find(producto_id)
        if producto:
            producto.activado = False
            db.session.commit()
            return True
        return False

    def all(self) -> List[Producto]:
        """Obtiene todos los productos activados."""
        return db.session.query(Producto).filter(Producto.activado == True).all()