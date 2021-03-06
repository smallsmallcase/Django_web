# @Time    : 2017/10/31 14:37
# @Author  : Jalin Hu
# @File    : forms.py
# @Software: PyCharm
from django import forms
from first_app.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
