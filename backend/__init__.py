from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')  # Jika Anda ingin menggunakan Jinja2 template engine
    config.add_route('home', '/')
    config.add_route('products', '/products')  # Rute untuk produk
    config.scan()
    return config.make_wsgi_app()
    config.add_route('add_product', '/products/add')
    config.add_route('delete_product', '/products/delete/{id}')
    config.add_route('update_product', '/products/update/{id}')
    config.add_route('partial_update_product', '/products/partial_update/{id}')
    config.add_route('add_purchase', '/purchases/add')
