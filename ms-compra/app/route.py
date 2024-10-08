from flask import Blueprint, request
from app.service import CompraService
from app.mapping import CompraSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

compra_bp = Blueprint('compra', __name__)

compra_service = CompraService()
compra_schema = CompraSchema()
response_schema = ResponseSchema()

@compra_bp.route('/compras', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    compras = compra_service.all()
    data = compra_schema.dump(compras, many=True)
    response_builder.add_message("Compras encontradas").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@compra_bp.route('/compras/add', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    compra = compra_schema.load(request.json)
    data = compra_schema.dump(compra_service.add(compra))
    response_builder.add_message("Compra creada").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

@compra_bp.route('/compras/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = compra_service.delete(id)
    if data:
        response_builder.add_message("Compra deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Compra not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404