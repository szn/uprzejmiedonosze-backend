import falcon

from reporting.web.images.context import ContextImageResource
from reporting.web.images.details import DetailsImageResource


def setup(container):
    container.add_service(app, name='web.wsgi.app')
    container.add_service(
        context_image_resource,
        name='web.images.context_resource',
    )
    container.add_service(
        details_image_resource,
        name='web.images.details_resource',
    )
    setup_routing(container)


def app(container):
    return falcon.API()


def context_image_resource(container):
    return ContextImageResource()


def details_image_resource(container):
    return DetailsImageResource()


def setup_routing(container):
    container('web.wsgi.app').add_route(
        '/image/context',
        container('web.images.context_resource'),
    )
    container('web.wsgi.app').add_route(
        '/image/details',
        container('web.images.details_resource'),
    )
