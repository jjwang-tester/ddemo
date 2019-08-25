from django.conf.urls import url
from aclassview import views

urlpatterns = [

    # 类视图的路由
    url(r'^aclassview/$', views.LoginView.as_view()),

]