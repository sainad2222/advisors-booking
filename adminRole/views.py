from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Advisor
from .serializers import AdvisorSerializer


class AdvisorViewClass(APIView):
    def post(self, request):
        serializedData = AdvisorSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
