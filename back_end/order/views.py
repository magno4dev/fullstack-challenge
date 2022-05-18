from .serializer import OrderSerializer, CategorySerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Pedido, Category

# Create your views here.


class OrderApi(APIView):

    @api_view(['GET'])
    def get(request):
        pedidos = Pedido.objects.all()
        serializer = OrderSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def find(request, pk):
        try:
            pedido = Pedido.objects.get(pk=pk)
        except pedido.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = OrderSerializer(pedido)
            return Response(serializer.data)

    @api_view(['POST'])
    def post(request):

        dead_line_trated = request.data.get('dead_line')[0:10]

        pedido = Pedido.objects.create( 
            contact_name= request.data.get('contact_name'),
            contact_tel= request.data.get('contact_tel'),
            order_description= request.data.get('order_description'),
            real_state_agency= request.data.get('real_state_agency'),
            company= request.data.get('company'),
            dead_line= dead_line_trated,
            category_id= request.data.get('category'))

        pedido.save()
        return Response({"message":"Criado Com Sucesso"}, status=status.HTTP_201_CREATED)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            pedido = Pedido.objects.get(pk=pk)
        except pedido.DoesNotExist:
            return HttpResponse(status=404)

        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def update(request, pk):
        try:
            pedido = Pedido.objects.get(pk=pk)
        except pedido.DoesNotExist:
            return HttpResponse(status=404)

        serializer = OrderSerializer(pedido, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class CategoryApi(APIView):

    @api_view(['GET'])
    def get(self):
        categorias = Category.objects.all()
        serializer = CategorySerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def find(request, pk):
        try:
            categoria = Category.objects.get(pk=pk)
        except categoria.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = OrderSerializer(categoria)
            return Response(serializer.data)

    @api_view(['POST'])
    def post(self, request, *args, **kwargs):

        data = {
            'description': request.data.get('description')
        }

        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except category.DoesNotExist:
            return HttpResponse(status=404)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def update(request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except category.DoesNotExist:
            return HttpResponse(status=404)

        serializer = CategorySerializer(category, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_204_NO_CONTENT)
