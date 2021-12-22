from flask import json

from config import config

MARPICO = 'MARPICO'

def set_product(params, **kwargs):    
    provider = params.get('provider', None)
    # Get images
    images = params.get('imagenes')
    image_group_aux = params.get('imagen', None)

    image_group_dt: str = image_group_aux["imagen"]["file"] if image_group_aux else None
    image_lg = images[0]["imagen"]["file"] if images and images[0] else None
    image = images[0]["imagen"]["file_md"] if images and images[0] else None
    image_sm = images[0]["imagen"]["file_sm"] if images and images[0] else None 
    size = f'Largo: {params.get("medidas_largo", "Sin datos")}, Alto: {params.get("medidas_alto", "-")}, Ancho: {params.get("medidas_ancho", "Sin datos")}'

    product_output = { }
    if params:
        product_output['provier_name'] = config[provider]['NAME']
        product_output['referency_id'] = params.get('codigo', None)
        product_output['cod_product'] = params.get('familia', None)
        product_output['category'] = params.get('familia', None)
        product_output['name'] = params.get('descripcion_comercial', None)
        product_output['description'] = params.get('descripcion_larga', None)
        product_output['colors'] = params.get('color_nombre', None)

        product_output['size'] = size
        product_output['prints'] = params.get('tecnica_marca_tecnica', None)
        product_output['printsArea'] = params.get('area_impresion', None)
        product_output['packing'] =  params.get('empaque_unds_caja', None)

        product_output['discount'] = float(params.get('descuento', None))
        product_output['cost'] = float(params.get('precio', None))
        product_output['cost_after_discount'] = float(params.get('precio', 0)) - float(params.get('descuento', 0))
        product_output['inventory'] = params.get('inventario', None)

        product_output['image'] = image
        product_output['image_sm'] = image_sm
        product_output['image_lg'] = image_lg
        product_output['image_group'] = image_group_dt

        product_output['detail'] = params.get('descripcion_larga', None)
        product_output['material'] = params.get('material', None)
        product_output['more_info'] = json.dumps(params)
    
    return product_output
