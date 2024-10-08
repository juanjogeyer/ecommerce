from app.repository import CompraRepository
from app.model import Compra
from typing import List

repository = CompraRepository()

class CompraService:

    def add_compra(self, compra: Compra) -> Compra:
        return repository.add_compra(compra)

    def all(self) -> List[Compra]:
        return repository.all()