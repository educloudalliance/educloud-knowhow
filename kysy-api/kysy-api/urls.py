from django.conf.urls import patterns, include, url
from api import views, urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'api.views.api_root', name='api-root'),
    url(r'^v1/', include('api.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
