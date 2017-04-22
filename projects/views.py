from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import _get_login_redirect_url
from django.contrib.sites.shortcuts import get_current_site
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django_filters.views import FilterView
from django.db.models import signals
from projects.form import ThesisInfoAddForm
from projects.models import Notice, ThesisInfo


@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if redirect_authenticated_user and request.user.is_authenticated:
        redirect_to = _get_login_redirect_url(request, redirect_to)
        if redirect_to == request.path:
            raise ValueError(
                "Redirection loop for authenticated user detected. Check that "
                "your LOGIN_REDIRECT_URL doesn't point to a login page."
            )
        return HttpResponseRedirect(redirect_to)
    elif request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            views.auth_login(request, form.get_user())
            return HttpResponseRedirect('/projects/index')
        else:
            form = authentication_form(request)
        current_site = get_current_site(request)

        context = {
            'form': form,
            redirect_field_name: redirect_to,
            'site': current_site,
            'site_name': current_site.name,
        }
        if extra_context is not None:
            context.update(extra_context)
        return TemplateResponse(request, template_name, context)


class ThesisInfoListView(FilterView):
    def get_queryset(self):
        if self.request.user.username == 'admin':
            query_set = ThesisInfo.objects.all()
        if self.request.user.username == 'wangkai1':
            query_set = ThesisInfo.objects.filter(user=self.request.user)
        else:
            query_set = ThesisInfo.objects.all()
        return query_set
    def get_paginate_by(self, queryset):
        return self.paginate_by

class NoticeListView(FilterView):
    def get_paginate_by(self, queryset):
        return self.paginate_by

class MeetingInfoListView(FilterView):
    def get_paginate_by(self, queryset):
        return self.paginate_by

@login_required
def indexView(request):
        return render(request, 'projects/index.html')

def add(request):
    template = 'projects/thesisInfo/add.html'
    if request.method == 'POST':
        form = ThesisInfoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/thesisInfoList')
    else:
        form = ThesisInfoAddForm()
    return render(request, template, {'form': form})

def upload(request):
    template = 'projects/thesisInfo/update.html'
    if request.method == 'POST':
        form = ThesisInfoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/thesisInfoList')
    else:
        form = ThesisInfoAddForm()
    return render(request, template, {'form': form})



        # @receiver(signals.post_init, sender=Notice)
# def project_init_signal(instance, sender, **kwargs):
#     instance.__noticeid = instance.pk
#     instance.__meetingInfo = instance.meetingInfo
#     instance.__message = instance.message
#
# @receiver(signals.post_save, sender=Notice)
# def notice_post_save(instance, created, raw, update_fields,sender, **kwargs):