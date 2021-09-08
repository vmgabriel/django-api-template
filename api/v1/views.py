"""Views API V1"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions


class HelloViewSet(viewsets.ViewSet):
    def hello(self, request):
        return Response({"message": "Hello World"})


hello_data = HelloViewSet.as_view({"get": "hello"})
