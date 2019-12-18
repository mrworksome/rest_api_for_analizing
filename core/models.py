from django.db import models

# Create your models here.
import uuid

# Create your models here.
from django.db.models import CASCADE
from django.contrib.postgres.fields import JSONField

from core.enum import SexEnum, StateEnum


class Entity(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    sex = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in SexEnum], null=False, default=SexEnum.NOT_STATED)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    bdate = models.CharField(max_length=100, null=True)
    graduation = models.CharField(max_length=500, null=True)
    hometown = models.CharField(max_length=200, null=True)
    university_name = models.CharField(max_length=200, null=True)
    education_form = models.CharField(max_length=100, null=True)
    education_status = models.CharField(max_length=100, null=True)
    relation = models.CharField(max_length=200, null=True)
    interests = models.TextField(null=True)
    activities = models.TextField(null=True)
    movies = models.TextField(null=True)
    tv = models.TextField(null=True)
    games = models.TextField(null=True)
    books = models.TextField(null=True)
    about = models.TextField(null=True)
    occupation = models.TextField(null=True)
    personal = models.TextField(null=True)
    career = models.TextField(null=True)
    schools = models.TextField(null=True)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    entities = models.ManyToManyField(Entity)
    status_task = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in StateEnum], null=False, default=StateEnum.CREATED)
    created_at = models.DateTimeField(max_length=200, auto_now_add=True, null=True)
    updated_at = models.DateTimeField(max_length=200, auto_now=True)


class Result(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    task_id = models.ForeignKey(Task, on_delete=CASCADE)
    result = JSONField()
    timestamp = models.DateTimeField(max_length=200, auto_now_add=True, null=True)
