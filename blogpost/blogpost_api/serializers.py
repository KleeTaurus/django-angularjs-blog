from rest_framework import serializers
import models


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPost
