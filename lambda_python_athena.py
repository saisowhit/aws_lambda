

import time
import boto3

query = 'SELECT complained_email_address FROM complain_count WHERE ingest_timestamp >= NOW() - interval '3' day AND application_id = '123456789' GROUP BY complained_email_address;'
DATABASE = 'pinpoint_events'
output='s3://pinpoint-events-data/'
path='application_1/complaints'

def lambda_handler(event, context):
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            # first {} contains the output variable, then adds a '/' character for the directory and then the path variable
            'OutputLocation': "{}/{}".format(output, path),
        }
    )
    return response
    return