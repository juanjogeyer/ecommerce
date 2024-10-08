from app.model import Producto
from marshmallow import validate, fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    precio = fields.Float(required=True, validate=validate.Range(min=0))
    activado = fields.Boolean(default=True)
    
    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)