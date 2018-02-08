from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'symmetrical - InstagramUser'

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name = 'followrs'

    )

    def __str__(self):
        return self.name

    def followers(self):
        #자신을 following하고 있는 사람들을 리턴
        #문자열이 아닌 쿼리 자체
        class Meta:
            verbose_name_plural = 'symmetrical - followers'
        return self.name