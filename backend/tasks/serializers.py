from dataclasses import fields
from rest_framework import serializers
from tasks.models import Category


class CateforySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["created_by"]
