from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from typing import List
from app import db
from app.model import Stock

class StockRepository:

    def all(self) -> List[Stock]:
        return db.session.query(Stock).all()

    def add(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock

    def update(self, producto_id: int, cantidad: float, tipo_transaccion: int) -> Stock:
        #Actualiza el stock de un producto agregando una transacción de entrada (1) o salida (2).
        transaccion = Stock(
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
    
    def delete(self, stock: Stock) -> None:
        db.session.delete(stock)
        db.session.commit()
        return None
    
    def find(self, id: int) -> Stock:
        return db.session.query(Stock).filter(Stock.id == id).one_or_none()