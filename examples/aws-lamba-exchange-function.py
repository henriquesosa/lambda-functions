import urllib
import json
import boto3

def lambda_handler(event, context):
  request = "API URL HERE"
  response = json.loads(request)

  ses.boto3.client('ses')

  email_from = "johndoe@email.com"
  email_to = "johndoe2@email.com"
  subject = "Exchange rate"
  body = "Dollar: U${0}". format(response['field'])

  return ses.send_email(
    Source = email_from,
    Destination = {
      "ToAddresses" : [email_to]
    },
    Message = {
      "Subject": {
        "Charset" : "UTF-8",
        "Data" : subject
      },
      "Body": {
        "Html" : {
          "Charset" : "UTF-8",
          "Data" : body
        }
      }
    }
  )