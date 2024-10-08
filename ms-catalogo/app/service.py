from app.model import Producto
from app.repository import ProductoRepository
from typing import List, Optional

repository = ProductoRepository()

class ProductoService:

    def save(self, producto: Producto) -> Producto:
        """Crea y guarda un nuevo producto."""
        return repository.save(producto)

    def update(self, producto: Producto, id: int) -> Producto:
        """Actualiza un producto existente."""
        return repository.update(producto, id)

    def delete(self, producto_id: int) -> None:
        """Elimina (desactiva) un producto."""
        producto = repository.find(producto_id)
        if not producto:
            raise ValueError("Producto no encontrado.")
        repository.delete(producto_id)

    def all(self) -> List[Producto]:
        """Devuelve todos los productos activados."""
        return repository.all()

    def find(self, id: int) -> Optional[Producto]:
        """Busca un producto por su ID."""
        return repository.find(id)