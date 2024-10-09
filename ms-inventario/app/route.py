from flask import Blueprint, request
from marshmallow import ValidationError
from app.service import StockService
from app.mapping import StockSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

inventario_bp = Blueprint('inventario', __name__)

response_schema = ResponseSchema()
stock_schema = StockSchema()
stock_service = StockService()

@inventario_bp.route('/inventario', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = stock_schema.dump(stock_service.all(), many=True)
    response_builder.add_message("Inventario found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@inventario_bp.route('/inventario', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        stock = stock_schema.load(request.json)
        data = stock_schema.dump(stock_service.save(stock))
        response_builder.add_message("Inventario added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@inventario_bp.route('/inventario/update', methods=['POST'])
def update():
    response_builder = ResponseBuilder()
    # Carga y valida los datos con StockSchema
    data = stock_schema.load(request.json)
    
    producto_id = data.get("producto_id")
    cantidad = data.get("cantidad")
    tipo_transaccion = data.get("entrada_salida")

    try:
        transaccion = stock_service.update_stock(producto_id, cantidad, tipo_transaccion)
        # Serializa la respuesta con StockSchema
        transaccion_data = stock_schema.dump(transaccion)
        response_builder.add_message("Stock actualizado").add_status_code(200).add_data(transaccion_data)
        return response_schema.dump(response_builder.build()), 200
    except ValueError as e:
        response_builder.add_message(str(e)).add_status_code(400)
        return response_schema.dump(response_builder.build()), 400

@inventario_bp.route('/inventario/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = stock_service.delete(id)
    if data:
        response_builder.add_message("Inventario deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Inventario not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404