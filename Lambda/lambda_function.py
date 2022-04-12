import boto3
import json
import psycopg2

s3_client = boto3.client('s3')
redshiftdb_client = boto3.client('redshift')

def lambda_handler(event, context):
    # TODO implement

    # get bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    # get file name
    file_name = event['Records'][0]['s3']['object']['key']

    s3_object = s3_client.object(Bucket=bucket, Key=file_name)

    s3FileReader = s3_object['Body'].read()
    s3Dict = json.loads(s3FileReader)

    # redshift database
    from_path = "s3://{}/{}".format(s3_bucket, s3_key)
    print("from path {}".format(from_path))
    Access_key = os.getenv('AWS_Access_key')
    Access_Secrete = os.getenv('AWS_Access_Secrete')
    dbname = os.getenv('dbname')
    host = os.getenv('host')
    user = os.getenv('user')
    password = os.getenv('password')
    tablename = os.getenv('tablename')

    HOST = "redshift-cluster-3760.redshift.amazonaws.com"
    PORT = "5439"
    DATABASE = "dev"
    USERNAME = "awsuser"
    PASSWORD = "XYZ"
    TABLE = "listingTable"

    connection = psycopg2.connect(dbname = dbname,
                             host = host,
                             port = '5439',
                             user = user,
                             password = password)
