def row_to_dict(row):
    # Convierte la fila en un diccionario utilizando el método .__dict__
    return {key: value for key, value in row.__dict__.items() if not key.startswith('_')}