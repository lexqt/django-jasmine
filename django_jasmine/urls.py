import os

from django.conf.urls import *
from django.conf import settings
from django.views import static

from views import run_tests

static_root = os.path.join(os.path.dirname(__file__), 'static')


def jasmine_rsc(request, prefix, package, path):
    return static.serve(request, os.path.join(package, prefix, path),
                 document_root=settings.JASMINE_TEST_DIRECTORY)


urlpatterns = patterns('django.views',
    url(r'^rsc/(?P<prefix>\w+)/(?P<package>\w+)/(?P<path>.*)$', jasmine_rsc, name='jasmine_rsc'),
    url(r'^fixtures/(?P<path>.*)$', static.serve, {
        'document_root': os.path.join(
            settings.JASMINE_TEST_DIRECTORY, "fixtures",
        ),
    }, name='jasmine_fixtures'),
    url('^(?P<package>.*)$', run_tests, name='jasmine_test_overview'),
)
