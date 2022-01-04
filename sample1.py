import boto3

rdsData = boto3.client('rds-data')

cluster_arn = 'arn:aws:rds:us-east-1:548985610555:cluster:paei'
secret_arn = 'arn:aws:secretsmanager:us-east-1:548985610555:secret:paei-rds-YFVbvv'
database_name = 'paei'


response = rdsData.execute_statement(
      resourceArn = cluster_arn,
      secretArn = secret_arn,
      database = database_name,
      sql = 'show tables')

print(response)

