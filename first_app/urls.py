# @Time    : 2017/10/29 15:55
# @Author  : Jalin Hu
# @File    : urls.py
# @Software: PyCharm
'''定义first_app的url模式'''
from django.conf.urls import url
from . import views
urlpatterns = [
    # 主页
    url(r'^$', view=views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$', view=views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', view=views.topic, name='topic'),
    # 添加新的主题
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 添加主题下面的内容
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 编辑内容
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]