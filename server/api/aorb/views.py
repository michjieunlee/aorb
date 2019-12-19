# from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AorB
from .serializers import AorbSerializer


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET', 'POST'])
# @login_required(login_url='/login')
def AorbView(request):
    if request.method == 'GET':
        aorbs = AorB.objects.all()
        serializer = AorbSerializer(aorbs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AorbSerializer(
            data=json.loads(request.body.decode("utf-8")))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(request)
        # serializer.data['user'] = request.user

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
