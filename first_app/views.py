from django.shortcuts import render
from .models import Topic, Entry
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    '''学习笔记主页'''
    return render(request, 'index.html')


def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    '''显示单个主题及其所有条目'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # “－”指定按降序排列
    content = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', content)


def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
         #  如果未提交数据：创建新的表单
        form = TopicForm()
    else:
         #  POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save() # 如果是合法的表单，则将它写入数据库
            return HttpResponseRedirect(reverse('first_app:topics'))

    context = {'form':form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    '''在特定主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        #  如果未提交数据，创建新表单
        form = EntryForm()
    else:
        #  POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('first_app:topic', args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request, 'new_entry.html', context)


def edit_entry(request, entry_id):
    #  编辑既有的条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('first_app:topic', args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'edit_entry.html', context)