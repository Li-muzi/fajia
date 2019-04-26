from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def index(request):
    return JsonResponse({'code': 0, 'data': "Hello, world. You're at the polls index.", 'msg': '成功'})
