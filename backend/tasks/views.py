from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import Category

from tasks.serializers import CateforySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CateforySerializer
    queryset = Category.objects.all()
