from __future__ import print_function
import boto3
import json
import os
from datetime import datetime
from botocore.exceptions import ClientError

#def lambda_handler(event,context):
print('00000')
SENDER = "xwu247@gmail.com"
RECIPIENT = "xwu247@gmail.com"
CONFIGURATION_SET = "ConfigSet"
AWS_REGION = "us-east-1"
SUBJECT = "Analysis Result"
print('1111')
    # The email body for recipients with non-HTML email clients.
BODY_TEXT = ('joy'
              )
CHARSET = "UTF-8"
client = boto3.client('ses',region_name=AWS_REGION)
try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,

        )
except ClientError as e:
        print('error')
else:
        print("sent successfully!"),
        print(response['ResponseMetadata']['RequestId'])

#lambda_handler(1,1)









