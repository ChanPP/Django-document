# Generated by Django 2.0.2 on 2018-02-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0005_instagramuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramuser',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='many_to_many.InstagramUser'),
        ),
    ]
