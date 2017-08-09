# coding: utf-8
from django.contrib import admin


from . import models


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
