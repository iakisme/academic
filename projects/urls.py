from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from django.contrib.auth import views
from projects.filters import ThesisInfoFilter, MeetingInfoFilter, NoticeFilter
from projects.form import ThesisInfoAddForm, MeetingInfoAddForm, NoticeAddForm
from .models import ThesisInfo, MeetingInfo,Notice
from .views import *

app_name = 'projects'

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'projects/myuser/login.html'},name='userLogin'),
    url(r'^logout/$', views.logout, {'template_name': 'projects/myuser/login.html'}, name='logout'),

    url(r'^index$', indexView, name='index'),

    #thesisInfo
    url(r'^thesisInfoList$',
        ThesisInfoListView.as_view(model=ThesisInfo, filterset_class=ThesisInfoFilter, template_name='projects/thesisInfo/list.html',
                                 paginate_by=7),name='thesisInfoList'),
    url(r'^thesisInfoAdd$',add, name='thesisInfoAdd'),
    url(r'^thesisInfo/(?P<pk>[0-9]+)/$', DetailView.as_view(model=ThesisInfo, template_name='projects/thesisInfo/detail.html'),
        name='thesisInfoDetail'),
    url(r'^(?P<pk>[0-9]+)/updatethesisInfo$', UpdateView.as_view(model=ThesisInfo, form_class=ThesisInfoAddForm,
                                                                 template_name='projects/thesisInfo/update.html',
                                                                 success_url=reverse_lazy('projects:thesisInfoList')),
        name='thesisInfoUpdate'),
    url(r'^(?P<pk>[0-9]+)/updatethesisInfo$', UpdateView.as_view(model=ThesisInfo, form_class=ThesisInfoAddForm,
                                                                 template_name='projects/thesisInfo/update.html',
                                                                 success_url=reverse_lazy('projects:thesisInfoList')),
        name='thesisInfoReview'),
    url(r'^(?P<pk>[0-9]+)/updatethesisInfo$', UpdateView.as_view(model=ThesisInfo, form_class=ThesisInfoAddForm,
                                                                 template_name='projects/thesisInfo/update.html',
                                                                 success_url=reverse_lazy('projects:thesisInfoList')),
        name='thesisInfoCheck'),
    url(r'^(?P<pk>[0-9]+)/deletethesisInfo$',
        DeleteView.as_view(model=ThesisInfo, success_url=reverse_lazy('projects:thesisInfoList')), name='thesisInfoDelete'),
    #meetingInfo
    url(r'^meetingInfoList$',
        MeetingInfoListView.as_view(model=MeetingInfo, filterset_class=MeetingInfoFilter,
                                   template_name='projects/meetingInfo/list.html',
                                   paginate_by=7), name='meetingInfoList'),
    url(r'^meetingInfoAdd$',
        CreateView.as_view(model=MeetingInfo, template_name='projects/meetingInfo/add.html',
                           form_class=MeetingInfoAddForm,
                           success_url=reverse_lazy('projects:meetingInfoList')), name='meetingInfoAdd'),
    url(r'^meetingInfo/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=MeetingInfo, template_name='projects/meetingInfo/detail.html'),
        name='meetingInfoDetail'),
    url(r'^(?P<pk>[0-9]+)/updatemeetingInfo$', UpdateView.as_view(model=MeetingInfo, form_class=MeetingInfoAddForm,
                                                                 template_name='projects/meetingInfo/update.html',
                                                                 success_url=reverse_lazy('projects:meetingInfoList')),
        name='meetingInfoUpdate'),
    url(r'^(?P<pk>[0-9]+)/deletemeetingInfo$',
        DeleteView.as_view(model=MeetingInfo, success_url=reverse_lazy('projects:meetingInfoList')),
        name='meetingInfoDelete'),
    #notice
    url(r'^noticeList$',
        NoticeListView.as_view(model=Notice, filterset_class= NoticeFilter,
                                   template_name='projects/notice/list.html',
                                   paginate_by=7), name='noticeList'),
    url(r'^noticeAdd$',
        CreateView.as_view(model=Notice, template_name='projects/notice/add.html',
                           form_class=NoticeAddForm,
                           success_url=reverse_lazy('projects:noticeList')), name='noticeAdd'),
    url(r'^notice/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=Notice, template_name='projects/notice/detail.html'),
        name='meetingInfoDetail'),
    url(r'^(?P<pk>[0-9]+)/updatenotice$', UpdateView.as_view(model=Notice, form_class=NoticeAddForm,
                                                                 template_name='projects/notice/update.html',
                                                                 success_url=reverse_lazy('projects:noticeList')),
        name='noticeUpdate'),
    url(r'^(?P<pk>[0-9]+)/deletenotice$',
        DeleteView.as_view(model=Notice, success_url=reverse_lazy('projects:noticeList')),
        name='noticeDelete'),
]
