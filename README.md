# amrap-wod-generator
AMRAP WOD Generator:
* creates a random AMRAP-based WOD
* generates a cool image containing the exercises of the day
* uploads the img to a GCP bucket
* tweets it to your account (if you want to)

## Environment variables
* `LOGS_FOLDER_PATH`: where logs are saved.
* `APP_NAME`: `amrap-wod-generator` for example.
* `IMGS_FOLDER`: where images are stored.

GCP info:
* `PROJECT_NAME`: GCP project name
* `BUCKET_NAME`: GCP bucket name
* `CLIENT_ID`: GCP client ID
* `CLIENT_EMAIL`: GCP clien email
* `PRIVATE_KEY_ID`: GCP private key ID
* `PRIVATE_KEY`: GCP private key
* `DESTINATION_BLOB`: `wod.png` for example
  
If you want to tweet it:
* `TWITTER_CONSUMER_KEY`: your Twitter consumer key.
* `TWITTER_CONSUMER_SECRET`: your Twitter consumer secret.
* `TWITTER_ACCESS_TOKEN`: your Twitter access token.
* `TWITTER_ACCESS_TOKEN_SECRET`: your Twitter access token secret.

The program will also try to import the `settings` module with this same information. You can create it by copying and pasting the available `seetings.py.sample` file, renaming it to `settings.py` with your actual preferences and credentials.

## Resulting image example
![wod-image](http://www.gaizkadc.com/wod.png "WOD image")

## Run it!
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# To just generate the AMRAO WOD image
python amrap-wod-generator.py

# Add the --tweet flag to tweet it
python amrap-wod-generator.py --tweet

deactivate
```

## Docker
To build the Docker image run:
```
docker build -f docker/Dockerfile .
```

Or just pull it:
```
docker pull gaizkadc/amrap-wod-generator:latest
```

## Important considerations
I'm from Spain (and I speak Spanish,) so the tweet text in the repo comes in Spanish. You may want to change that. Same for the Docker image, of course.