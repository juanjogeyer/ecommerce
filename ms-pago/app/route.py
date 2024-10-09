from flask import Blueprint, request
from app.service import PagoService
from app.mapping import PagoSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

pago_bp = Blueprint('pago', __name__)

pago_service = PagoService()
pago_schema = PagoSchema()
response_schema = ResponseSchema()

@pago_bp.route('/pagos', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = pago_schema.dump(pago_service.all(), many=True)
    response_builder.add_message("Pagos found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@pago_bp.route('/pagos/add', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    pago = pago_schema.load(request.json)
    data = pago_schema.dump(pago_service.add(pago))
    response_builder.add_message("Pago creado").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

@pago_bp.route('/pagos/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = pago_service.delete(id)
    if data:
        response_builder.add_message("Pago deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Pago not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404