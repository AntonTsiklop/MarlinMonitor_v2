# Generated by Django 4.1.4 on 2023-03-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_alter_tableab_imei'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TableBB',
        ),
        migrations.DeleteModel(
            name='TableRB',
        ),
        migrations.RenameField(
            model_name='tableab',
            old_name='FmtID',
            new_name='FormatID',
        ),
        migrations.RenameField(
            model_name='tableab',
            old_name='lat',
            new_name='Latitude',
        ),
        migrations.RenameField(
            model_name='tableab',
            old_name='lon',
            new_name='Longtitude',
        ),
    ]