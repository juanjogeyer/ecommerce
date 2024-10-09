from marshmallow import Schema, fields, post_load
from app.model import Stock

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_transaccion = fields.DateTime(required=True)
    cantidad = fields.Float(required=True)
    entrada_salida = fields.Integer(required=True)  # 1: entrada, 2: salida

    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)