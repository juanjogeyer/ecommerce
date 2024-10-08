from app import db
from app.model import Pago

class PagoRepository:

    def pay(self, pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago

    def delete(self, pago: Pago) -> None:
        db.session.delete(pago)
        db.session.commit()