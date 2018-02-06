# Generated by Django 2.0.2 on 2018-02-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_auto_20180205_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(related_name='_facebookuser_friends_+', to='many_to_many.FacebookUser')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', through='many_to_many.PostLike', to='many_to_many.User'),
        ),
    ]
