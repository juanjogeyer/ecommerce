from app.model import Pago
from app.repository import PagoRepository

repository = PagoRepository()

class PagoService:

    def pay(self, pago: Pago) -> Pago:
        return repository.pay(pago)

    def delete(self, pago_id: int) -> None:
        repository.delete(pago_id)