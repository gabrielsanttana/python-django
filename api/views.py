from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
  def get(self, request, format=None):
    django = "Django"

    return Response({'message': 'Hello,' + django})
