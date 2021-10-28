# Generated by Django 3.2.8 on 2021-10-28 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]