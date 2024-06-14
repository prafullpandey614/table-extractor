from xmlrpc.client import ResponseError
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status,response
from .serializers import FileSerializer
from .utils import extract_data
from .models import File

class UploadFileAPIView(APIView):
    
    def post(self,request,*args, **kwargs):
        data = request.data
        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            file_inst = serializer.save()
            print(serializer.data)
            extract_data(file_inst.file.path,file_inst)
            print(file_inst.extracted_table_txt)
            return response.Response("Successfully uploaded",status=status.HTTP_200_OK)
            
        return response.Response("Invalid File",status=status.HTTP_400_BAD_REQUEST)
    
    
class GetExtractedTables(APIView):
    def get(self,request,id,*args, **kwargs):
        obj = File.objects.get(id=id)
        serl = FileSerializer(obj)
        
        return response.Response(serl.data,status=status.HTTP_200_OK)
    