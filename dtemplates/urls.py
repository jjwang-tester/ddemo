from django.conf.urls import url
from dtemplates import views

urlpatterns = [

    url(r'^GetTemplates/$', views.GetTemplates.as_view())

]