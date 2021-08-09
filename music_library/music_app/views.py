from django.http.response import Http404
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#Show a list of songs with an option to create a new song to be added to the list.
class SongList(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retreive details, update details, or delete details of a song.
class SongDetail(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except:
            Song.DoesNotExist
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SongLikes(APIView):
    
    def get(self, request, pk):
        song = self.get_objects(pk)
        song.likes += 1
        song.save()
        serializer = SongSerializer(song)
        return Response(serializer.data)
