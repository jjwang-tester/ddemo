from django.conf.urls import url
from adbs import views
urlpatterns= [
    url(r'^adbs/$',views.Adbs.as_view())

]