"""
Standalone test runner for Observations plugin
"""
import os
import sys

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE='obs.tests.dummy_options_module',
                   ROOT_URLCONF='obs.urls',
                   STATIC_URL='/assets/',
                   STATIC_ROOT='static',
                   STATICFILES_FINDERS=(
                       'django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       'compressor.finders.CompressorFinder',),
                   COMPRESS_ROOT='/tmp/',
                   MIDDLEWARE=(
                       'django.middleware.common.CommonMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'opal.middleware.AngularCSRFRename',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware',
                       'opal.middleware.DjangoReversionWorkaround',
                       'reversion.middleware.RevisionMiddleware',
                       'axes.middleware.FailedLoginMiddleware',
                   ),
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'django.contrib.staticfiles',
                                   'compressor',
                                   'opal',
                                   'opal.tests',
                                   'obs',),
)

from opal.core import application
class Application(application.OpalApplication):
    pass


from obs.tests import dummy_options_module

import django
django.setup()

from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['obs', ])
if failures:
    sys.exit(failures)
