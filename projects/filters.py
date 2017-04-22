import django_filters

from projects.models import ThesisInfo, MeetingInfo, Notice


class ThesisInfoFilter(django_filters.FilterSet):
    # company_name = django_filters.CharFilter(name='company_name',lookup_expr='contains',label="公司名称:")
    # company_type = django_filters.ChoiceFilter(name='company_type',choices=Agents.COMPANY_TYPE_CHOICES,label="公司类型:")
    # company_qualification = django_filters.ChoiceFilter(name='company_qualification',choices=Agents.COMPANY_QUALIFICATION_CHOICES,label="公司资质:")
    class Meta:
        model = ThesisInfo
        fields = {}

class MeetingInfoFilter(django_filters.FilterSet):
    class Meta:
        model = MeetingInfo
        fields = {}

class NoticeFilter(django_filters.FilterSet):
    class Meta:
        model = Notice
        fields = {}
