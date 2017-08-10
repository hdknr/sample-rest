# coding: utf-8
import django_filters
from rest_framework import viewsets, filters
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly as BasePerm
)

from django.contrib.auth.models import User
from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [BasePerm, ]


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [BasePerm, ]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    # permission_classes = [BasePerm, ]
