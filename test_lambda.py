import json

def lambda_handler (event, context):
    print ("Hello my name is Kulbhushan")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda! from my code')
    }
