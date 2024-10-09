from app.repository import StockRepository
from app.model import Stock

repository = StockRepository()

class StockService:

    def all(self) -> list[Stock]:
        return repository.all()

    def add(self, stock: Stock) -> Stock:
        return repository.add(stock)

    def update(self, producto_id: int, cantidad: float, tipo_transaccion: int) -> Stock:
        #Actualiza el stock de un producto.
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        # Si es salida, verifica que haya suficiente stock
        if tipo_transaccion == 2:
            stock_actual = repository.get_stock(producto_id)
            if stock_actual < cantidad:
                raise ValueError("No hay suficiente stock disponible para realizar la salida.")
        
        return repository.update_stock(producto_id, cantidad, tipo_transaccion)

    def delete(self, id: int) -> bool:
        stock = self.find(id)
        if stock:
            repository.delete(stock)
            return True
        else: 
            return False

    def find(self, id: int) -> Stock:
        return repository.find(id)