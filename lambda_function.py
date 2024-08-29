import json
import time

def lambda_handler(event, context):
    print("Politicas y tratamientos de los datos: mucho texto from github el dia de la presentacion \n - Fecha y hora:", time.strftime("%Y-%m-%d %H:%M:%S"))
    response = {
        'statusCode': 200,
        'body': json.dumps('Política de tratamiento de datos aceptada')
    }

    user_acceptance = event.get('acceptance', False)
    
    if user_acceptance:
        response['body'] = json.dumps('Aceptacion registrada')
    else:
        response['statusCode'] = 400
        response['body'] = json.dumps('Aceptacion no recibida')

    return response
