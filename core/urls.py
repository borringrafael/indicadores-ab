from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(
                                    template_name='core/index.html'),
                                    name='core.index',
                                    ),
    url(r'^metas/$', metas, name='core.metas'),
]
