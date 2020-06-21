from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Goods
from django.db.models import Max
from .serializers import GoodsSerializer

@api_view(['GET', 'POST'])
def get_availible(request, format=None):
  """
  List all goods with the exception of goods with the price of more than 20
  """
  if request.method == 'GET':
    # Models sets the max price to 20
    goods = Goods.objects.aggregate(Max('price'))
    serializer = GoodsSerializer(goods,context={'request': request}, many=True)
    return Response(serializer.data) #Return JSON
  elif request.method == 'POST':
    serializer = GoodsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def good_detail(request, pk):
  """
  Retrieve, update goods instance.
  """
  try:
    good = Goods.objects.get(pk=pk)
  except Goods.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ProductSerializer(good, context={'request': request})
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = GoodsSerializer(product, data=request.data,context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

# class GoodsDetail(APIView):

#   def get_object(self, pk):
#     try:
#       return Goods.objects.get(pk=pk)
#     except Goods.DoesNotExist:
#       raise Http404  

#   def get_availible(self, request, format=None):
#     goods = self.get_object(pk)
#     goods = GoodsSerializer(goods)
#     return Response(goods.data) 

#   def set_limit(self, request, pk, format=None):
#     goods = self.get_object(pk)
#     serializer = GoodsSerializer(goods, data=request.DATA)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
#     #return response(serializer.errors.status=status.HTTP_400_BAD_REQUEST)    
