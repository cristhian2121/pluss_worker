from config import config

MARPICO = 'MARPICO'

def set_product(product_input):
    product_output = { }
    if product_input:
        image_url = f"{config['MPPROMOCIONALES']['URL_IMAGE']}{product_input.get('codigoProd')}.{config['EXTENSION']['JPG']}"
        cod_product = product_input.get('codigoProd')
        image = image_url if cod_product else None 
        
        product_output['provier_name'] = config['MPPROMOCIONALES']['NAME']
        product_output['referency_id'] = product_input.get('referencia') or None
        product_output['cod_product'] = product_input.get('codigoProd') or None
        product_output['name'] = product_input.get('descripcion') or None
        product_output['description'] = product_input.get('descLarga') or None
        product_output['size'] = product_input.get('medidas') or None
        product_output['colors'] = product_input.get('color') or None
        product_output['prints'] = product_input.get('marca') or None
        product_output['printsArea'] = product_input.get('areaImpresion') or None
        product_output['packing'] = product_input.get('empaque') or None
        product_output['discount'] = product_input.get('descuento') or None
        product_output['cost_after_discount'] = product_input.get('precioDescuento') or None
        product_output['image'] = image
        product_output['inventory'] = product_input.get('existencias') or None
        product_output['cost'] = product_input.get('vlrUnitario') or None
        product_output['detail'] = product_input.get('descLarga') or None
        product_output['material'] = product_input.get('material') or None
        product_output['more_info'] = product_input

        return product_output
    return product_output


