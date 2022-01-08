from django.shortcuts import render
from testapp.models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from testapp.serializers import StudentSerializers
from rest_framework import serializers
from rest_framework import status
# Create your views here.

class StudentAPIViewForID(APIView):
    def get_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except:
            stud=None
        return stud
    def get(self,request,pk,*args,**kwargs):
        if pk:
            stud=self.get_by_id(pk)
            if stud is None:
                return Response({'msg':'Student details not found, Please provides valid id.'},status=status.HTTP_400_BAD_REQUEST)
            serializer=StudentSerializers(stud)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'msg':'Student details not found, Please provides valid id.'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,*args,**kwargs):
        stud=self.get_by_id(pk)
        if stud is None:
                return Response({'msg':'Student details not found, Please provides valid id.'},status=status.HTTP_400_BAD_REQUEST)
        stud.delete()
        return Response({'msg':'Deleted Sucessfully'},status=status.HTTP_200_OK)
    def put(self,request,pk,*args,**kwargs):
        stud=self.get_by_id(id=pk)
        if stud is None:
                return Response({'msg':'Student details not found, Please provides valid id.'},status=status.HTTP_400_BAD_REQUEST)
        serializer=StudentSerializers(data=request.data,instance=stud)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,*args,**kwargs):
        stud=self.get_by_id(id=pk)
        if stud is None:
                return Response({'msg':'Student details not found, Please provides valid id.'},status=status.HTTP_400_BAD_REQUEST)
        serializer=StudentSerializers(data=request.data,instance=stud,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentAPIView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        if qs is None:
            return Response({'msg':'Student details not found.'},status=status.HTTP_400_BAD_REQUEST)
        serializer=StudentSerializers(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        stud=StudentSerializers(data=request.data)
        if stud is None:
            return Response({'msg':'Student details not found.'},status=status.HTTP_400_BAD_REQUEST)
        if stud.is_valid():
            stud.save()
            return Response(stud.data,status=status.HTTP_201_CREATED)
        else:
            return Response(stud.errors,status=status.HTTP_400_BAD_REQUEST)