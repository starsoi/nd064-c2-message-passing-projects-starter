def register_routes(api, app, root="api"):
    from app.location.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
