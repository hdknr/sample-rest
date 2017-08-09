# coding: utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', ]


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
        fields = ['code', 'name', ]


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'created_at', 'status', 'author', ]
