
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-090dgzzhx+^8al1mbfidpa4d+-0vr1w4emw3iop&^-wjd#nqgd'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'products_database',
        'USER': 'root',
        'PASSWORD': 'qazwsx2022',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
