# coding: utf-8

from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'status', viewsets.StatusViewSet)
router.register(r'articles', viewsets.ArticleViewSet)
