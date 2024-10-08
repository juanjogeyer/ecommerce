from typing import List
from app import db
from app.model import Compra

class CompraRepository:

    def add_compra(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra

    def all(self) -> List[Compra]:
        return Compra.query.all()