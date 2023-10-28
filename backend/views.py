from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='products', renderer='json')
def products_view(request):
    products = [
        {"id": 1, "name": "Product 1", "price": 10.0},
        {"id": 2, "name": "Product 2", "price": 15.0},
        {"id": 3, "name": "Product 3", "price": 20.0}
    ]
    return products

products = []  # List produk sederhana sebagai contoh

@view_config(route_name='add_product', request_method='POST', renderer='json')
def add_product_view(request):
    data = json.loads(request.body)  # Menerima data produk dalam format JSON
    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }
    products.append(new_product)
    return {"message": "Product added successfully", "product": new_product}

@view_config(route_name='delete_product', request_method='DELETE', renderer='json')
def delete_product_view(request):
    product_id = int(request.matchdict['id'])
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {"message": f"Product with ID {product_id} deleted successfully"}
    return {"message": f"Product with ID {product_id} not found"}

@view_config(route_name='update_product', request_method='PUT', renderer='json')
def update_product_view(request):
    product_id = int(request.matchdict['id'])
    data = json.loads(request.body)  # Menerima data perubahan dalam format JSON
    for product in products:
        if product['id'] == product_id:
            product['name'] = data.get('name', product['name'])
            product['price'] = data.get('price', product['price'])
            return {"message": f"Product with ID {product_id} updated successfully", "product": product}
    return {"message": f"Product with ID {product_id} not found"}

@view_config(route_name='partial_update_product', request_method='PATCH', renderer='json')
def partial_update_product_view(request):
    product_id = int(request.matchdict['id'])
    data = json.loads(request.body)  # Menerima data perubahan dalam format JSON
    for product in products:
        if product['id'] == product_id:
            product['name'] = data.get('name', product['name'])
            product['price'] = data.get('price', product['price'])
            return {"message": f"Product with ID {product_id} updated partially", "product": product}
    return {"message": f"Product with ID {product_id} not found"}

purchases = []  # List pembelian sederhana sebagai contoh

@view_config(route_name='add_purchase', request_method='POST', renderer='json')
def add_purchase_view(request):
    data = json.loads(request.body)  # Menerima data pembelian dalam format JSON
    new_purchase = {
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity")
    }
    purchases.append(new_purchase)
    return {"message": "Purchase added successfully", "purchase": new_purchase}

