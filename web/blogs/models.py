# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Status(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Article Status')
        verbose_name_plural = _('Article Status')

    def __str__(self):
        return self.name


class Article(models.Model):
    status = models.ForeignKey(Status)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title
