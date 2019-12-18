from django.http import Http404
from rest_framework import serializers

from core.models import Entity, Task, Result


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    entities = EntitySerializer(many=True, write_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        entities = validated_data.pop('entities')
        entities = [Entity.objects.create(**entity) for entity in entities]
        task = Task.objects.create(**validated_data)
        task.entities.add(*entities)
        return task


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        exclude = ['id', 'timestamp', 'task_id_id']

