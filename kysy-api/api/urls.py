from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('api.views',
    url(r'^users/$', 'user_list', name='user-list'),
    url(r'^questions/$', views.QuestionList.as_view(), name='question-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
