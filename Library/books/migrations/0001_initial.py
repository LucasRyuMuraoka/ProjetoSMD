# Generated by Django 4.2.1 on 2023-05-28 04:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('idBook', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('releaseYear', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('publishingCompany', models.CharField(max_length=255)),
                ('createAt', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
