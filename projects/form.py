from django import forms

from projects.models import *

class ThesisInfoAddForm(forms.ModelForm):
    class Meta:
        model = ThesisInfo
        fields = "__all__"
        widgets = {
            'create_time': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class MeetingInfoAddForm(forms.ModelForm):
    class Meta:
        model = MeetingInfo
        fields = "__all__"
        widgets = {
            'start_time': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_time': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class NoticeAddForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
        widgets = {
            'create_time': forms.DateInput(attrs={'class': 'datepicker'}),
        }