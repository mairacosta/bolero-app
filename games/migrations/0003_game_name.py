# Generated by Django 3.2.9 on 2021-11-23 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211122_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='', max_length=63, verbose_name='nome'),
            preserve_default=False,
        ),
    ]
