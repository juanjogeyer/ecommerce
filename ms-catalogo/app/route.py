from flask import Blueprint, request
from app.service import ProductoService
from app.mapping import ProductSchema, ResponseSchema
from app.mapping.response_message import ResponseBuilder

catalogo_bp = Blueprint('catalogo', __name__)

product_schema = ProductSchema()
response_schema = ResponseSchema()
product_service = ProductoService()

# Get: Muestra JSON con todos los productos
@catalogo_bp.route('/productos', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = product_schema.dump(product_service.all(), many=True)
    response_builder.add_message("Productos encontrados").add_status_code(200).add_data(data)

    return response_schema.dump(response_builder.build()), 200

# Post: Crea un nuevo producto a partir de un JSON
@catalogo_bp.route('/productos/add', methods=['POST'])
def add_product():
    response_builder = ResponseBuilder()
    product = product_schema.load(request.json)
    data = product_schema.dump(product_service.save(product))
    response_builder.add_message("Producto creado").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

# Delete: Elimina un producto a partir de su id
@catalogo_bp.route('/productos/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Producto eliminado").add_status_code(200).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200

# Get: JSON con los datos del producto buscado por id
@catalogo_bp.route('/productos/<int:id>', methods=['GET'])
def find(id):
    response_builder = ResponseBuilder()
    data = product_schema.dump(product_service.find(id))
    if data:
        response_builder.add_message("Producto encontrado").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Producto NO encontrado").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404

# Put: Actualiza un producto a partir de un JSON
@catalogo_bp.route('/productos/<int:id>', methods=['PUT'])
def update_product(id: int):
    product = product_schema.load(request.json)
    response_builder = ResponseBuilder()
    data = product_schema.dump(product_service.update(product, id))
    if data:
        response_builder.add_message("Producto actualizado").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Producto NO actualizado - ID no encontrado").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404