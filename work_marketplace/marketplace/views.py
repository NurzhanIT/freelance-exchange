from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace.models import Executor
from marketplace.serializers import ExecutorModelSerializer
from marketplace.services import get_object_by_pk, delete_obj_by_pk, is_auth


class ExecutorView(APIView):

    def get(self, request, *args, **kwargs):
        pk: int = kwargs.get('pk')
        if pk:
            executor = get_object_by_pk(Executor, pk)
            return Response({"executor": ExecutorModelSerializer(executor).data})
        else:
            executor = get_object_by_pk(Executor)
            return Response({"executors": ExecutorModelSerializer(executor, many=True).data})

    def post(self, request):
        is_auth(request)
        request.data['user'] = request.user.id
        serializer = ExecutorModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Executor.objects.filter(user=serializer.validated_data['user']):
            return Response({"res": "user already exists"})
        serializer.save()
        return Response({"res": serializer.data})

    def delete(self, request, *args, **kwargs):
        is_auth(request)
        pk: int = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Missed a pk argument for delete method!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            delete_obj_by_pk(Executor, pk)
        except Exception as e:
            Response({"got error": str(e)})
        return Response("Success  deleted", status=status.HTTP_200_OK)
