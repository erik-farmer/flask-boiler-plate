def register_api(view, url, blueprint, pk='id', pk_type='int'):
    # Index
    blueprint.add_url_rule(url, view_func=view, methods=['GET'])
    # Create
    # blueprint.add_url_rule(url, view_func=view, methods=['POST'])
    # Resource Urls
    # blueprint.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
