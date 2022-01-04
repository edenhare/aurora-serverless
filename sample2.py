import boto3
import os
import time
from datetime import datetime


rdsData = boto3.client('rds-data')
rds=boto3.client('rds')

cluster_arn = 'arn:aws:rds:us-east-1:548985610555:cluster:paei'
secret_arn = 'arn:aws:secretsmanager:us-east-1:548985610555:secret:paei-rds-YFVbvv'
database_name = 'paei'

print(f"{datetime.now()} sleeping to catch cluster with 0 capacity units")
while True:
      response2 = rds.describe_db_clusters(DBClusterIdentifier=database_name)
      if response2['DBClusters'][0]['Capacity'] > 0:
            print(f"{datetime.now()} sleeping 300 seconds capacity = {response2['DBClusters'][0]['Capacity']}")
            time.sleep(300)
      else:
            break
print(f"{datetime.now()} capacity = {response2['DBClusters'][0]['Capacity']}")

# we have to be ready to retry on error becasue the other end might be "sleeping"
retry=0
while True:
      print(f"{datetime.now()} retry: {retry}")
      try:
            response = rdsData.execute_statement(
                  resourceArn = cluster_arn,
                  secretArn = secret_arn,
                  database = database_name,
                  sql = 'show tables')
      except Exception as error:
            response2 = rds.describe_db_clusters(DBClusterIdentifier=database_name)
            print(f"{datetime.now()} exception: {error}")
            print(f"{datetime.now()} capacity = {response2['DBClusters'][0]['Capacity']}")
            retry += 1
      else:
            print(f"{datetime.now()} {response}")
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                  print("done")
                  exit(0)

