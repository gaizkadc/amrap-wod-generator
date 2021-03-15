from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


def upload_amrap_wod_to_gcp(logger, img_path):
    logger.info('uploading amrap wod img to gcp')

    credentials_dict, bucket_info_dict = get_gcp_info(logger)

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project=bucket_info_dict['project_name'])

    bucket = client.bucket(bucket_info_dict['bucket_name'])
    blob = bucket.blob(bucket_info_dict['destination_blob'])
    blob.upload_from_filename(img_path)

    logger.info('file {} uploaded to {}'.format(img_path, bucket_info_dict['bucket_name'] + '/' + bucket_info_dict['destination_blob']))


def get_gcp_info(logger):
    try:
        logger.info('retrieving gcp credentials from settings')
        import settings
        project_name = settings.PROJECT_NAME
        bucket_name = settings.BUCKET_NAME
        client_id = settings.CLIENT_ID
        client_email = settings.CLIENT_EMAIL
        private_key_id = settings.PRIVATE_KEY_ID
        private_key = settings.PRIVATE_KEY
        destination_blob = settings.DESTINATION_BLOB
    except ModuleNotFoundError as error:
        logger.info('unable to import settings')
        logger.info(error)
        project_name = os.getenv('PROJECT_NAME')
        bucket_name = os.getenv('BUCKET_NAME')
        client_id = os.getenv('CLIENT_ID')
        client_email = os.getenv('CLIENT_EMAIL')
        private_key_id = os.getenv('PRIVATE_KEY_ID')
        private_key = os.getenv('PRIVATE_KEY')
        destination_blob = os.getenv('DESTINATION_BLOB')

    credentials= {
        'type': 'service_account',
        'client_id': client_id,
        'client_email': client_email,
        'private_key_id': private_key_id,
        'private_key': private_key,
    }

    bucket_info = {
        'project_name': project_name,
        'bucket_name': bucket_name,
        'destination_blob': destination_blob
    }

    return credentials, bucket_info
