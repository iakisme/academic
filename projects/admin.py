from django.contrib import admin

# Register your models here.
from projects.models import *

admin.site.register(userInfo)
admin.site.register(ThesisInfo)
admin.site.register(MeetingInfo)
admin.site.register(Notice)

