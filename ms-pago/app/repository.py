from typing import List
from app import db
from app.model import Pago

class PagoRepository:

    def add(self, pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago

    def delete(self, pago: Pago) -> None:
        db.session.delete(pago)
        db.session.commit()

    def all(self) -> List[Pago]:
        return db.session.query(Pago).all()