import json
import time

def lambda_handler(event, context):
    # Ejemplo de respuesta al aceptar la política de tratamiento de datos
    print("Politicas y tratamientos de los datos: mucho texto from github 6 \n - Fecha y hora:", time.strftime("%Y-%m-%d %H:%M:%S"))
    response = {
        'statusCode': 200,
        'body': json.dumps('Política de tratamiento de datos aceptada')
    }
    
    # Aquí puedes manejar la lógica de aceptación
    user_acceptance = event.get('acceptance', False)
    
    if user_acceptance:
        # Guardar en la base de datos o enviar un evento
        response['body'] = json.dumps('Aceptación registrada')
    else:
        response['statusCode'] = 400
        response['body'] = json.dumps('Aceptación no recibida')

    return response
