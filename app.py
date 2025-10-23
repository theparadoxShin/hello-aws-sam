import json

def lambda_handler(event, context):
    """
    A simple AWS Lambda function that returns a JSON response.
    """
    print('Event received:', event)

    # Response
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Hello from Lambda!'})
    }