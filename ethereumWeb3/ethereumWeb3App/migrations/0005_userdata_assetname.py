# Generated by Django 4.0.4 on 2022-06-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereumWeb3App', '0004_userdata_ipfsurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='AssetName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
