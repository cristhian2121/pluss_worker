

def set_product(product_input):
    product_output = { }
    if product_input:
        product_output['referency_id'] = product_input.get('referencia') or None
        product_output['provier_name'] = MPPROMOCIONALES
        product_output['name'] = product_input.get('descripcion') or None
        product_output['illustration'] = product_input.get('imagen') or None
        product_output['detail'] = product_input.get('descLarga') or None
        product_output['measurements'] = product_input.get('medidas') or None
        product_output['mark_type'] = product_input.get('marca') or None
        product_output['color'] = product_input.get('color') or None
        product_output['material'] = product_input.get('material') or None
        product_output['more_info'] = product_input
        return product_output
    return product_output

MPPROMOCIONALES = 'mppromocionales'

