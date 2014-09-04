from django.db import models


# Create your models here.
class BlogPost(models.Model):
        title = models.CharField(max_length=128)
        content = models.TextField()
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-created']


class Comment(models.Model):
        blogpost = models.ForeignKey(BlogPost, editable=False,
                                     related_name='comments')
        comment = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
