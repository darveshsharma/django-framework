from django.shortcuts import render

# Create your views here.
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class ContactAPIView(APIView):
   def get(self, request):
      contacts=Contact.objects.all()
      serializer =ContactSerializer(contacts, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer =ContactSerializer(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):
   def get_object(self,id):
      try:
         return Contact.objects.get(id=id)
   
      except Contact.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
   
   def get(self, request, id):
      contact =self.get_object(id)
      serializer = ContactSerializer(contact)
      return Response(serializer.data)

   def put(self, request, id):
      contact =self.get_object(id)
      serializer = ContactSerializer(contact, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, id):
      contact = self.get_object(id)
      contact.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

