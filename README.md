# amrap-wod-generator
AMRAP WOD Generator:
* creates a random AMRAP-based WOD
* generates a cool image containing the exercises of the day
* tweets it to your account

To create the image, [Postkit's API](https://postkit.co/) is used. It is free up to 100 requests each month, which shouldn't be a problem.


## Environment variables
* `LOGS_FOLDER_PATH`: where logs are saved.
* `APP_NAME`: `amrap-wod-generator` for example.
* `POSTKIT_TEMPLATE_ID`: template ID provided by Postkit when a template is created.
* `POSTKIT_TOKEN`: Potkit's API token.
* `IMG_SIZE`: `707x890` for example.
* `IMGS_FOLDER`: where images are stored.
* `POSTKIT_ENDPOINT`: `https://api.postkit.co/make` as of today.
* `TWITTER_CONSUMER_KEY`: your Twitter consumer key.
* `TWITTER_CONSUMER_SECRET`: your Twitter consumer secret.
* `TWITTER_ACCESS_TOKEN`: your Twitter access token.
* `TWITTER_ACCESS_TOKEN_SECRET`: your Twitter access token secret.

## Run it!
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python amrap-wod-generator.py

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