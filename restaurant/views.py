from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookingTable,MenuTable
from .serializers import BookingTableSerializer,MenuTableSerializer
# Create your views here.

class Bookingview(APIView):

    def get(self,request):
        items = BookingTable.objects.all()
        serializer = BookingTableSerializer(items,many=True)
        return Response (serializer.data)
    
class MenuView(APIView):
    def post(self,request):
        serializer = MenuTableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
    