# -*- coding: utf-8 -*-

import sys, os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH))
sys.path.insert(0, os.path.join(PROJECT_PATH, 'apps'))
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Mateusz Dargacz', 'mateuszdargacz@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jonasz',  # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',  # Empty for localhost through$
        'PORT': '',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        },
    }

}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'apps', 'cms_plugins', 'attractions', 'locale'),
    os.path.join(PROJECT_ROOT, 'apps', 'cms_plugins', 'facilities', 'locale'),
    os.path.join(PROJECT_ROOT, 'apps', 'cms_plugins', 'gallery', 'locale'),
    os.path.join(PROJECT_ROOT, 'apps', 'cms_plugins', 'slider', 'locale'),
    os.path.join(PROJECT_ROOT, 'templates', 'locale'),

)
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7ml=w+v%3_o5q-2tuu-+z3mvy*z&amp;qd8&amp;^-s1vgjt^lcmwib2$1'

# List of callables that know how to import templates from various sources.


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # REVOLUTION^^   SLIDER MIDDLEWARE

)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'))
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # cms
    'south',
    'menus',
    'mptt',
    'sekizai',
    'cms',
    'djangocms_text_ckeditor',
    'djangocms_googlemap',
    'cms.admin',
    #thidparty
    'easy_thumbnails',
    'adminsortable',
    'bootstrapform',
    'modeltranslation',
    #my apps
    'apps.apartaments',
    'apps.reservation',
    'apps.cms_plugins.attractions',
    'apps.cms_plugins.slider',
    'apps.cms_plugins.gallery',
    'apps.cms_plugins.facilities',
    'apps.cms_plugins.contact_form',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# DJango CMS
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

CMS_TEMPLATES = (
    ('cms/sites/gallery.html', 'Galeria'),
    ('cms/sites/about.html', u'Strona główna'),
    ('cms/sites/atractions.html', 'Atrakcje'),
    ('cms/sites/surroundings.html', 'Otoczenie'),
    ('cms/sites/contact.html', 'Kontakt'),
    ('cms/sites/empty.html', 'Pusty'),
)
LANGUAGES = [
    ('pl', 'Polish'),
    ('en', 'English'),
]
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True

#Emails
CONTACT_EMAIL_TO = ['pensjonatjonasz@op.pl', 'mateuszdargacz@gmail.com']
#email settings
EMAIL_FOOTER = u"\n\nPensjonat Jonasz\nDębki\ntel. 723 573 620, 602 444 508\npensjonatjonasz@op.pl\nNumer konta:  do wypełnienia"
DEFAULT_FROM_EMAIL = 'Pensjonat  "Jonasz" <rezerwacja@jonasz.pl>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rezerwacja@jonasz.pl'

#TODO UNCOMMENT!!!!!!!!!!!
# try:
#     execfile('%s/project/local_settings.py' % PROJECT_PATH)
# except IOError:
#     pass
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jonasz.db',  # Or path to database file if using sqlite3.

    }

}