# Generated by Django 4.1.4 on 2023-03-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_delete_tableabdefective'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableab',
            name='FmtID',
            field=models.IntegerField(default=0),
        ),
    ]
