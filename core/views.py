import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from core.enum import StateEnum
from core.models import Entity, Task, Result
from core.serializer import EntitySerializer, TaskSerializer, ResultSerializer


class EntityViewSet(generics.ListAPIView):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ResultViewSet(generics.CreateAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        entities = r.get('entities')
        for entity in entities:
            if 'name' not in entity or 'phone' not in entity or 'email' not in entity:
                return JsonResponse({'error': 'missing fields'}, status=402)

        task = Task.objects.create()
        for entity in entities:
            _entity = Entity.objects.create(**entity)
            task.entities.add(_entity)

        # response = requests.post(url, data=payload)
        # if response.status == 200:
            task.status_task = StateEnum.RUNNING
            task.save()
        return JsonResponse({'task_id': task.id})


@csrf_exempt
def get_result(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)

    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer_task = TaskSerializer(task)
        task_status = serializer_task.data.get('status_task')
        if task_status == 0:
            content = {"status": "Task not started"}
            # status with out content !!!
            return JsonResponse(content, status=204)
        elif task_status == 1:
            return JsonResponse({"status": "Task is running"}, status=206)
        elif task_status == 2:
            result = Result.objects.filter(task_id_id=task_id).first()
            task = Task.objects.filter(task_id_id=task_id).first()
            task.status_task = StateEnum.COMPLETED
            return JsonResponse(result.result)
        else:
            return JsonResponse({'Invalid status value'})


@csrf_exempt
def create_collected_data(request):
    if request.method == 'POST':
        r = json.loads(request.body)

        for i in r.get('entities'):
            _payload = {**i}
            if 'personal' in i and i.get('personal'):
                _payload.update({
                    'personal': json.dumps(i.get('personal'))
                })
            elif 'occupation' in i and i.get('occupation'):
                _payload.update({
                    'occupation': json.dumps(i.get('occupation'))
                })
            elif 'career' in i and i.get('career'):
                _payload.update({
                    'career': json.dumps(i.get('career'))
                })
            elif 'schools' in i and i.get('schools'):
                _payload.update({
                    'schools': json.dumps(i.get('schools'))
                })
            _entity = Entity.objects.create(**_payload)

        # response = requests.post(url, data=r)
        # if response.status == 200:

        return JsonResponse({"status": "OK"})


@csrf_exempt
def get_analysis(request):
    if request.method == 'POST':
        r = json.loads(request.body)
        if 'task_id' not in r or 'result' not in r:
            return JsonResponse({"error": "Invalid input"}, status=405)
        Result.objects.create(task_id_id=r.get('task_id'), result=r.get('result'))
        return JsonResponse({"status": "OK"})
