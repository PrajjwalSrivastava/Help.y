# Generated by Django 3.1.4 on 2021-05-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngos',
            name='address',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ngos',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ngos',
            name='thumbnail',
            field=models.FileField(upload_to='images/'),
        ),
    ]
