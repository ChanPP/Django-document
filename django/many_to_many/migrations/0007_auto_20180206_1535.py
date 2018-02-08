# Generated by Django 2.0.2 on 2018-02-06 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0006_auto_20180206_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facebookuser',
            options={'verbose_name_plural': 'symmetrical_intermediate - FacebookUser'},
        ),
        migrations.AlterModelOptions(
            name='instagramuser',
            options={'verbose_name_plural': 'symmetrical - InstagramUser'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'Basic - Pizza'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'intermediate - Post'},
        ),
        migrations.AlterModelOptions(
            name='postlike',
            options={'verbose_name_plural': 'intermediate - PostLike'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Basic - Toppings'},
        ),
        migrations.AlterModelOptions(
            name='twitteruser',
            options={'verbose_name_plural': 'symmetrical_intermediate - TwitterUser'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'intermediate - User'},
        ),
    ]
