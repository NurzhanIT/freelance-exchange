from django.contrib.auth.models import AnonymousUser


def get_object_by_pk(obj, pk: int = None):
    if pk:
        return obj.objects.filter(pk=pk)[0]
    else:
        return obj.objects.all()


def delete_obj_by_pk(obj, pk: int):
    return obj.objects.filter(pk=pk).delete()


def is_auth(request):
    from rest_framework.response import Response
    if not request.user or isinstance(request.user, AnonymousUser):
        return Response({"detail": "Authentication credentials were not provided."})