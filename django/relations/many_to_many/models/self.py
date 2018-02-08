from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')
    class Meta:
        verbose_name_plural = 'symmetrical_intermediate - FacebookUser'

    def __str__(self):
        # friends_string = ''
        # for friend in self.friends.all():
        #     friends_string += friend.name
        #     friends_string += ','
        # friends_string = friends_string[:-2]
        # friends_string = ', '.join([friends.name for friend in self.friends.all()])
        friends_string = ', '.join(self.friedns.values_list('name', flat=True))

        return f'{self.name} (친구 : {friends_string})'
