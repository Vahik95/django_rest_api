import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from myapi.mixins import JsonResponseMixin

from .models import Update


class JsonCBV(View):
    def get(self, request):
        data = {
            "brand": "BMW",
            "model": "M5",
            "price": 25000,
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "brand": "BMW",
            "model": "M5",
            "price": 25000,
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            "user": obj.user.username,
            "content": obj.content,
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs) #, fields=('user', 'content')
        print(data)
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content,
        # }
        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')
