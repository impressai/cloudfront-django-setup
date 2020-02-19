How to serve static and media files for a django app through django-storages using CloudFront
===================================
This project is intended to demostrate the AWS CloudFront with the Django.

Setting up
------------

### Python version
	python2

### Install python requirements
	pip install -r requirements.txt


### Making migration
	python manage.py makemiragions
    python manage.py migration

### Check if its working
    python manage.py runserver

This will run the code with debug mode enabled now we need to run the code with the aws cloudfront.

### Assign the following values in the Setting file
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME
    STATIC_DISTRIBUTION_ID

### After setting the AWS values make debug mode FALSE
    DEBUG = false

### Collect static files to s3
    python manage.py collectstatic

### Run the code in DEBUG mode FALSE
    python manage.py runserver

### To test the public and private media file storage
Got to `http://localhost:8000/api/`
The private files api is in `http://localhost:8000/api/private_image`
The private files api is in `http://localhost:8000/api/public_image`

