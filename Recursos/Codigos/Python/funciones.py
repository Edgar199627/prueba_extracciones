
from dotenv import load_dotenv
import boto3
import os

def subir_a_s3(archivo_local, bucket, nombre_en_s3):
    ''''Esta funcion sube los archivos a s3
    '''
    s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)
                           
    try:
        s3.upload_file(
            Filename=archivo_local,
            Bucket=bucket,
            Key=nombre_en_s3
        )
        print(f"Archivo subido: {nombre_en_s3}")
    except Exception as e:
        print(f"Error: {e}")