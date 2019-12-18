# Generated by Django 2.2.7 on 2019-12-18 13:35

import core.enum
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('sex', models.CharField(choices=[(core.enum.SexEnum(0), 0), (core.enum.SexEnum(1), 1), (core.enum.SexEnum(2), 2)], default=core.enum.SexEnum(0), max_length=20)),
                ('country', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status_task', models.CharField(choices=[(core.enum.StateEnum(0), 0), (core.enum.StateEnum(1), 1), (core.enum.StateEnum(2), 2)], default=core.enum.StateEnum(0), max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, max_length=200, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, max_length=200)),
                ('entities', models.ManyToManyField(to='core.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, max_length=200, null=True)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Task')),
            ],
        ),
    ]
