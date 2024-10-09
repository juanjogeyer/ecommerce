from app.model import Producto
from app.repository import ProductoRepository
from typing import List

repository = ProductoRepository()

class ProductoService:

    def all(self) -> List[Producto]:
        return repository.all()

    def find_activo(self, id: int) -> Producto:
        return repository.find_activo(id)
    
    def add(self, producto: Producto) -> Producto:
        return repository.add_product(producto)