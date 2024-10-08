from flask import Blueprint, request
from app.service import InventarioService
from app.mapping import InventarioSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

inventario = Blueprint('inventario', __name__)

response_schema = ResponseSchema()
inventario_schema = InventarioSchema()
inventario_service = InventarioService()

# POST: Actualiza el stock de un producto (entrada o salida)
@inventario.route('/inventario/update', methods=['POST'])
def update_stock():
    response_builder = ResponseBuilder()

    # Carga y valida los datos con InventarioSchema
    data = inventario_schema.load(request.json)
    
    producto_id = data.get("producto_id")
    cantidad = data.get("cantidad")
    tipo_transaccion = data.get("entrada_salida")

    try:
        transaccion = inventario_service.update_stock(producto_id, cantidad, tipo_transaccion)
        # Serializa la respuesta con InventarioSchema
        transaccion_data = inventario_schema.dump(transaccion)
        response_builder.add_message("Stock actualizado").add_status_code(200).add_data(transaccion_data)
        return response_schema.dump(response_builder.build()), 200
    except ValueError as e:
        response_builder.add_message(str(e)).add_status_code(400)
        return response_schema.dump(response_builder.build()), 400

# GET: Devuelve el stock actual de un producto
@inventario.route('/inventario/stock/<int:producto_id>', methods=['GET'])
def get_stock(producto_id: int):
    response_builder = ResponseBuilder()

    stock = inventario_service.get_stock(producto_id)
    response_builder.add_message("Stock actual obtenido").add_status_code(200).add_data({"stock_actual": stock})
    
    return response_schema.dump(response_builder.build()), 200