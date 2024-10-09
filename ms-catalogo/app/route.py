from flask import Blueprint, request
from marshmallow import ValidationError
from app.service import ProductoService
from app.mapping import ProductSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

catalogo_bp = Blueprint('catalogo', __name__)

producto_schema = ProductSchema()
response_schema = ResponseSchema()
producto_service = ProductoService()

@catalogo_bp.route('/productos', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = producto_schema.dump(producto_service.all(), many=True)
    response_builder.add_message("Productos encontrados").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@catalogo_bp.route('/productos/add', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        producto = producto_schema.load(request.json)
        data = producto_schema.dump(producto_service.add(producto))
        response_builder.add_message("Producto added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@catalogo_bp.route('/productos/<int:id>', methods=['GET'])
def find_activo(id):
    response_builder = ResponseBuilder()
    data = producto_schema.dump(producto_service.find_activo(id))
    if data:
        response_builder.add_message("Producto encontrado").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Producto NO encontrado").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404