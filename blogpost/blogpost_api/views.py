from rest_framework import generics
import serializers
import models


# Create your views here.
class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogPostSerializer
    queryset = models.BlogPost.objects.all()


class BlogPostInstanceAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BlogPostSerializer
    queryset = models.BlogPost.objects.all()
