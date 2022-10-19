

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o!%z84!@+a7j5dt@#%5z00)dmkm##7c_wjg_ng6#ysk20-z7%@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'theblog',
    'members',
    'ckeditor',

    'social_django',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'ablog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'ablog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
#LOGIN_URL = '/login/oauth'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


#Add For Github
SOCIAL_AUTH_GITHUB_KEY = 'f733e57230039dce1939'
SOCIAL_AUTH_GITHUB_SECRET = 'd11556f474c2651a771b335ed43bdc4e39a31b0f'

#Add For Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '543506764317-nk4rg3cif40c3m2ibhq2jrecj2r3rjvb.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

#Add For LinkedIn
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '86pmhmlh6serp0'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'PbVrjiKUy1lhdOMV'

#Add For Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '512880760319701'
SOCIAL_AUTH_FACEBOOK_SECRET = '410f470862d0f4476221ca79f7246421'

#for extra info
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]
