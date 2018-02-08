from datetime import datetime
from django.db import models
from django.utils import timezone
__all__ = (
    'PostLike',
    'User',
    'Post',
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField('User', through='PostLike', related_name='like_posts')

    class Meta:
        verbose_name_plural = 'intermediate - Post'

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'intermediate - User'

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'intermediate - PostLike'

    def __str__(self):
        return '{title} {name} {date}'.format(
            title = self.post.title,
            name=self.user.name,
            date=datetime.strftime(datetime.timezone.localtime
                                   (self.created_date, '%Y, %m, %d')))