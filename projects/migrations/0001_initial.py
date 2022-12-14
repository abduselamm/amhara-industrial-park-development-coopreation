# Generated by Django 4.1 on 2022-09-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_name', models.CharField(max_length=200, null=True)),
                ('purpose', models.CharField(max_length=200, null=True)),
                ('cluster', models.CharField(max_length=200, null=True)),
                ('Investment_Capital', models.CharField(max_length=200, null=True)),
                ('Job_Creation', models.CharField(max_length=200, null=True)),
                ('Mayor_Approval_of_land', models.CharField(max_length=200, null=True)),
                ('Recieved_Land_Meter_square', models.CharField(max_length=200, null=True)),
                ('Industry_Village', models.CharField(max_length=200, null=True)),
                ('UPIN_Number', models.CharField(max_length=200, null=True)),
                ('Block_Number', models.CharField(max_length=200, null=True)),
                ('Parcel_Number', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
