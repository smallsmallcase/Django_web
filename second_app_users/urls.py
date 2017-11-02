# @Time    : 2017/11/1 17:53
# @Author  : Jalin Hu
# @File    : urls.py
# @Software: PyCharm
'''为应用程序users定义URL模式'''
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # 登录界面
    url(r'^login/$', login,{'template_name': 'users/login.html'}, name='login'),
    # 注销
    url(r'^logout/$',view=views.logout_view, name='logout'),
]