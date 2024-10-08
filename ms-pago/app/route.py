from flask import Blueprint, request
from app.service import PagoService
from app.mapping import PagoSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

pago_bp = Blueprint('pago', __name__)

pago_service = PagoService()
pago_schema = PagoSchema()
response_schema = ResponseSchema()

@pago_bp.route('/pagos/add', methods=['POST'])
def add_pago():
    response_builder = ResponseBuilder()
    pago = pago_schema.load(request.json)
    data = pago_schema.dump(pago_service.save(pago))
    response_builder.add_message("Pago creado").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

@pago_bp.route('/pagos/<int:id>', methods=['DELETE'])
def delete_pago(id):
    pago_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Pago eliminado").add_status_code(200).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200