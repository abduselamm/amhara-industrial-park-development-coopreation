# Generated by Django 4.1 on 2022-09-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='capital',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='request',
            name='jobcreation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='projectcluster',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='projectname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='purpose',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
