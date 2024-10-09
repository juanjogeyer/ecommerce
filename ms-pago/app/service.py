from app.model import Pago
from app.repository import PagoRepository

repository = PagoRepository()

class PagoService:

    def add(self, pago: Pago) -> Pago:
        return repository.add(pago)

    def delete(self, id: int) -> bool:
        pago = self.find(id)
        if pago:
            repository.delete(pago)
            return True
        else:
            return False

    def all(self) -> list[Pago]:
        return repository.all()

    def find(self, id: int) -> Pago:
        return repository.find(id)