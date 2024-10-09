from typing import List
from app import db
from app.model import Compra

class CompraRepository:

    def add(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra

    def all(self) -> List[Compra]:
        return db.session.query(Compra).all()

    def delete(self, compra: Compra):
        db.session.delete(compra)
        db.session.commit()