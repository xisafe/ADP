# coding:utf-8

from __future__ import unicode_literals
from datetime import datetime
from django.db import models
<<<<<<< HEAD

=======
import os

from ADP.settings import STATIC_URL

# Create your models here.
>>>>>>> github/master

# ctf题型分类
CATEGORY_CHOICES = (
    ("MISC", "安全杂项"),
    ("PPC", "编程类"),
    ("CRYPTO", "密码学类"),
    ("PWN", "溢出类"),
    ("REVERSE", "逆向工程类"),
    ("STEGA", "隐写类"),
    ("WEB", "Web漏洞类"),
)


class Ctf(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    # 可能会将题目详情改为富文本显示
    detail = models.CharField(verbose_name=u"题目详情", default="", max_length=300)
<<<<<<< HEAD
    images = models.CharField(verbose_name=u"题目镜像", default="wooyun:latest", max_length=50)
    port = models.IntegerField(verbose_name=u"开放端口", default=80)
=======
    url = models.CharField(verbose_name=u"题目链接", default="http://", max_length=100)
>>>>>>> github/master
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    source = models.CharField(max_length=100, verbose_name=u"题目来源", default="")
    degree = models.CharField(verbose_name=u"难度", max_length=2, choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")))
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
<<<<<<< HEAD
    image = models.ImageField(upload_to="ctf/%Y/%m", default=u"image/default.jpg", verbose_name=u"封面(240px*135px)")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    submit_num = models.IntegerField(default=0, verbose_name=u"答案提交次数")
=======
    image = models.ImageField(upload_to="ctf/%Y/%m", default=u"image/default.jpg", verbose_name=u"封面")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
>>>>>>> github/master
    success_num = models.IntegerField(default=0, verbose_name=u"成功夺旗人数")
    flag = models.CharField(default="", max_length=100, verbose_name=u"题目答案")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=7, verbose_name=u"题目类别")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=20, blank=True)
    score = models.IntegerField(default=10, verbose_name=u"题目分数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"CTF题目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


<<<<<<< HEAD
class Docker(models.Model):
    user = models.CharField(max_length=50, default="", verbose_name="用户")
    image = models.CharField(max_length=50, verbose_name=u"镜像", default="")
    port = models.IntegerField(verbose_name=u"映射端口", default=80)
    con_id = models.CharField(verbose_name=u"容器ID", default="", max_length=100)

    class Meta:
        verbose_name = u"容器信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


=======
>>>>>>> github/master
class BannerCtf(Ctf):
    class Meta:
        verbose_name = "轮播CTF题目"
        verbose_name_plural = verbose_name
        proxy = True
<<<<<<< HEAD
=======



>>>>>>> github/master
