# Generated by Django 2.2.1 on 2019-06-28 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacts',
        ),
    ]