#!/usr/bin/python3
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def index(request):
    code = 0
    data = "Hello, world. You're at the polls index."
    msg = "请求成功"
    result = {"code": code, "data": data, "msg": msg}
    return JsonResponse(result)
