# coding: utf-8
from django.contrib import admin


from . import models


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'updated_at', ]
