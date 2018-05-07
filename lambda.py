from __future__ import print_function

import json
import urllib.parse
import boto3
import os
from datetime import datetime
from botocore.exceptions import ClientError
from watson_developer_cloud import ToneAnalyzerV3
import requests
import urllib

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(response)
        print(response['Body'].read())
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
		
	#analysis
	tone_analyzer = ToneAnalyzerV3(
        username='25aff8c5-4afd-4b18-aed8-12bab8d78090',
        password='5dAUlipzhPdj',
        version='2017-09-26'
    )
    tone = tone_analyzer.tone(message, tones='emotion', content_type='application/json')
    #analysis = requests.post('https://gateway.watsonplatform.net/tone-analyzer/api', auth =('25aff8c5-4afd-4b18-aed8-12bab8d78090','5dAUlipzhPdj'), data = message)
    print(tone)
    
    #send email
	SENDER = "xwu247@gmail.com"
    RECIPIENT = "xwu247@gmail.com"
    CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "us-east-1"
    SUBJECT = "Analysis Result"
    
    BODY_TEXT = tone
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