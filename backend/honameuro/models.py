from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=100, default="생활", null=True)  # 주제


class IndivInfo(models.Model):
    title = models.CharField(max_length=200, null=True)  # 제목
    content = models.TextField(null=True)  # 내용
    name = models.CharField(max_length=100, null=True)  # 단체명
    topic = models.ForeignKey(Topic, default=1, on_delete=models.CASCADE)  # 주제
    max = models.PositiveSmallIntegerField(default=10, null=True)  # 최대 몇 명이 선택할 수 있나요?
    selected = models.PositiveSmallIntegerField(default=0, null=True)  # 몇 명이 선택했나요?


class VillageInfo(models.Model):
    title = models.CharField(max_length=200, null=True)  # 제목
    content = models.TextField(null=True)  # 내용
    name = models.CharField(max_length=100, null=True)  # 마을명(단체명)
    max = models.PositiveSmallIntegerField(default=10, null=True)  # 최대 몇 명이 선택할 수 있나요?
    selected = models.PositiveSmallIntegerField(default=0, null=True)  # 몇 명이 선택했나요?


class IndivTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 주제
    indiv = models.ForeignKey(IndivInfo, on_delete=models.CASCADE)  # 고른 사람
