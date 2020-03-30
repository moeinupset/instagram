
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9khf=nq25x&vz391w^^49-ext)_hinr8szhmh=@w5c-e225pqu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DB = {
    'NAME': 'instagram',
    'USER': 'test',
    'PASSWORD': 'test',
    'HOST': 'localhost',
    'PORT': '5432'
}