from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer

class Goods(APIView):

  def get_availible(self, request, format=None):
    goods = Goods.objects.filter(price <= 20)
    serializer = GoodsSerializer(goods, many=True)
    return Response(serializer.data) #Return JSON
  
  def set_limit(self, request, format=None):
    serializer = GoodsSerializer(data=request.DATA) # This is similar to Request.POST
    if serializer.is_valid():
      serializer.save()
      data = JSONParser().parse(stream)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoodsDetail(APIView):

  def get_object(self, pk):
    try:
      return Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
      raise Http404  

  def get_availible(self, request, format=None):
    goods = self.get_object(pk)
    goods = GoodsSerializer(goods)
    return Response(goods.data) 

  def set_limit(self, request, pk, format=None):
    goods = self.get_object(pk)
    serializer = GoodsSerializer(goods, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    #return response(serializer.errors.status=status.HTTP_400_BAD_REQUEST)    
