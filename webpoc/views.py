from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer, Login
from .serializers import customerSerializer, loginSerializer 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins




# Create your views here.
# @csrf_exempt
# def customer_detail(request, pk):
#     try:
#         detail = Customer.objects.get(pk=pk)
        
#     except Customer.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method =='GET':
#         serializer = customerSerializer(detail)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer= customerSerializer(detail, data=data) 

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         detail.delete()
#         return JsonResponse(status=204)
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = customerSerializer
    queryset = Customer.objects.all()

    lookup_field= 'id'

    def get(self,request, id= None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)   

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request,id)


class ArticleAPIView(APIView):
    def get(self,request):
        articles = Customer.objects.all()
        serializer = customerSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer= customerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method =='GET':
        articles = Customer.objects.all()
        serializer = customerSerializer(articles, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer= customerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Customer.objects.get(pk=pk)
        
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = customerSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer= customerSerializer(article, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
class ArticleAPIDetails(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article =self.get_object(id)
        serializer = customerSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article =self.get_object(id)
        serializer= customerSerializer(article, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article =self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 



def logindata(request):
    datalogin =  Customer.objects.get
    if request.method =='GET':
        serializer = loginSerializer(datalogin)
        return JsonResponse(serializer.data)       

