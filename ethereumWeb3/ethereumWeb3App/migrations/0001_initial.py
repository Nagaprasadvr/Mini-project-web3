# Generated by Django 4.0.4 on 2022-05-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('userKey', models.CharField(default='1234', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('index', models.IntegerField(default=0)),
                ('TypeOfData', models.CharField(blank=True, max_length=100, null=True)),
                ('IpfsHash', models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('TimeStamp', models.DateTimeField(blank=True, null=True, unique=True)),
                ('UploadTnxHash', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ethereumWeb3App.user')),
            ],
        ),
    ]