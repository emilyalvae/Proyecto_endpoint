import json
import mercadopago
import os


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])

    payment_data = json.loads(event['body'])

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    return {
        "statusCode": 201,
        "body": json.dumps(
            {
                "status": payment['status'],
                "detail": payment['detail'],
                "payment_method": payment['payment_method'],
                "id": payment['id']
            }
        )
    }