
import boto3 

rdsData = boto3.client('rds-data')

database = "paei"
cluster_arn = "arn:aws:rds:us-east-1:548985610555:cluster:paei"
secret_arn = "arn:aws:secretsmanager:us-east-1:548985610555:secret:paei-rds-YFVbvv"

c = 1
while True:

    print(f"request #{c} ", end='' )
    try:
        response1 = rdsData.execute_statement(
                    resourceArn = cluster_arn, 
                    secretArn = secret_arn, 
                    database = database,
                    sql = 'select * from assessments')
    except  Exception as error:
        print(f"execution failure: {error}")
    else:
        print("execution success")
        break
    c += 1

print (response1)
