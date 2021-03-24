# Generated by Django 3.1.7 on 2021-03-24 17:35

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_auto_20200829_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True),
        ),
    ]
