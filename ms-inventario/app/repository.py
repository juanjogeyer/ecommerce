from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from app import db
from app.model import Inventario

class InventarioRepository:

    def update_stock(self, producto_id: int, cantidad: float, tipo_transaccion: int) -> Inventario:
        #Actualiza el stock de un producto agregando una transacción de entrada (1) o salida (2).
        transaccion = Inventario(
            producto_id=producto_id,
            cantidad=cantidad,
            entrada_salida=tipo_transaccion
        )

        try:
            db.session.add(transaccion)
            db.session.commit()
            return transaccion
        except IntegrityError:
            db.session.rollback()
            raise
    
    def get_stock(self, producto_id: int) -> float:
        #Obtiene el stock actual de un producto sumando todas las transacciones de entrada y salida.
        #Las entradas suman al stock y las salidas restan del stock.
        stock_actual = db.session.query(
            func.sum(
                func.case(
                    [(Inventario.entrada_salida == 1, Inventario.cantidad),
                     (Inventario.entrada_salida == 2, -Inventario.cantidad)]
                )
            )
        ).filter(Inventario.producto_id == producto_id).scalar()

        return stock_actual or 0.0  # Retorna 0 si no hay transacciones