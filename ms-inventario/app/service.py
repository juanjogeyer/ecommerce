from app.repository import InventarioRepository
from app.model import Inventario

inventario_repository = InventarioRepository()

class InventarioService:
    def update_stock(self, producto_id: int, cantidad: float, tipo_transaccion: int) -> Inventario:
        #Actualiza el stock de un producto.
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        # Si es salida, verifica que haya suficiente stock
        if tipo_transaccion == 2:
            stock_actual = inventario_repository.get_stock(producto_id)
            if stock_actual < cantidad:
                raise ValueError("No hay suficiente stock disponible para realizar la salida.")
        
        return inventario_repository.update_stock(producto_id, cantidad, tipo_transaccion)
    
    def get_stock(self, producto_id: int) -> float:
        #Devuelve el stock actual de un producto.
        return inventario_repository.get_stock(producto_id)