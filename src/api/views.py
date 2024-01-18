from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import CheckList, CheckListItem
from django.views.decorators.csrf import csrf_exempt
from api.serializer import CheckListSerializer, CheckListItemSerializer
from rest_framework import status
# from rest_framework.status import status
# Create your views here.

class CheckListsAPIView(APIView):
    def get(self, request):
        data = CheckList.objects.all()

        serializer = CheckListSerializer(data, many=True)
        serialized_data = serializer.data

        return Response(serialized_data)
    



    def post(self, request, format=None):
        serializer = CheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response("ABC")


class CheckListAPIView(APIView):
    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        serializer = CheckListSerializer(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def put(self, request, pk):
        Checklist = self.get_object(pk)
        serializer = CheckListSerializer(Checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response("ABC")
    
    def delete(self, request, pk):
        CheckList = self.get_object(pk)
        CheckList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# CheckList Item Logic
    
# @csrf_exempt
class CheckListItemCreateAPIView(APIView):
    def post(self, request):
        serialized = CheckListItemSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            serialized_data = serialized.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class CheckListItemAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        serializer = CheckListItemSerializer(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def put(self, request, pk):
        Checklist = self.get_object(pk)
        serializer = CheckListItemSerializer(Checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        CheckList = self.get_object(pk)
        CheckList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    