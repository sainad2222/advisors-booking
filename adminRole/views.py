from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Advisor
from .serializers import AdvisorSerializer

"""
request: 
    name: String
    profile_url: Url
response:
    None
"""
class AdvisorViewClass(APIView):
    def post(self, request):
        print("ENTERED")
        serializedData = AdvisorSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializedData)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
