from rest_framework import serializers
import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QaUsers
        fields = ('userid','email')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QaPosts
        fields = ('postid','title','content')

