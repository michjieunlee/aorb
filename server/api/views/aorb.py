import json
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Aorb
from api.serializers import AorbSerializer


class AorbsView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all aorb cards.
        """
        aorbs = Aorb.objects.all()
        serializer = AorbSerializer(aorbs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a aorb card
        """
        serializer = AorbSerializer(
            data=json.loads(request.body.decode("utf-8")))

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AorbView(APIView):
    def get_object(self, id):
        try:
            return Aorb.objects.get(id=id)
        except Aorb.DoesNotExist:
            raise Http404

    def get(self, request, id):
        """
        Return a list of all aorb cards.
        """
        aorb = self.get_object(id)
        serializer = AorbSerializer(aorb)
        return Response(serializer.data)
