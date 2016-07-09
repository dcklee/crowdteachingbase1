from .settings import *

SITE_ID = 2
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['student.qsvisa.com','member.qsvisa.com','enlingo.com','enlingo.com.au','member.enlingo.com','member.enlingo.com.au','www.enlingo.com','www.enlingo.com.au']


ROOT_URLCONF = 'crowdteachingbase1.student_urls'

# Aliyun_OSS_Image_Service for thumbnails

ALIYUN_OSS_THUMBNAILS_URL = "//thumbnail.qsvisa.com/"

WSGI_APPLICATION = 'crowdteachingbase1.wsgi5.application'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "templates", "locale"),
]

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME_CROWD_TEACHING_TEST"),
        'USER': os.environ.get("DB_USER_CROWD_TEACHING_TEST"),
        'PASSWORD': os.environ.get("DB_PASSWORD_CROWD_TEACHING_TEST"),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}