from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class userInfo(models.Model):
    USER_TYPE = (
        (1,'管理员'),
        (2,'审稿员'),
        (3,'参会者')
    )
    type = models.IntegerField(verbose_name="用户类型",choices=USER_TYPE)
    user = models.OneToOneField(User)

class ThesisInfo(models.Model):
    STATUS = (
        (1,'通过'),
        (2,'不通过'),
    )
    theme = models.CharField(verbose_name="主题", max_length=100)
    headline = models.CharField(verbose_name="摘要", max_length=100)
    keyword = models.CharField(verbose_name="关键词", max_length=50)
    user = models.ForeignKey(User,verbose_name="用户")
    thesisUrl = models.FileField(verbose_name="论文保存地址", upload_to='projects/static/documents/%Y/%m/%d')
    auditStatus = models.IntegerField(verbose_name="审核状态", choices=STATUS,blank=True,null=True)
    reviewStatus = models.IntegerField(verbose_name="评审状态", choices=STATUS,blank=True,null=True)
    create_time = models.DateTimeField(verbose_name="创建时间",default='2017-4-23')
    modifyTime = models.DateTimeField(verbose_name="修改时间")

class MeetingInfo(models.Model):
    meeting_name = models.CharField(verbose_name="会议名称", max_length=100)
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    meeting_address = models.CharField(verbose_name="会议地址", max_length=100)
    meeting_plan = models.CharField(verbose_name="会议安排", max_length=500)
    create_time = models.DateTimeField(verbose_name="创建时间",default='2017-4-23')
    create_user = models.ForeignKey(User,verbose_name="创建人")
    def __str__(self):
        return self.meeting_name

class Notice(models.Model):
    message = models.CharField(verbose_name="信息内容",max_length=1000)
    meetingInfo = models.ForeignKey(MeetingInfo,verbose_name="会议")
    create_time = models.DateTimeField(verbose_name="创建时间",default='2017-4-23')