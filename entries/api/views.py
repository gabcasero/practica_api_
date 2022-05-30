from rest_framework.views import APIView
from rest_framework.response import Response
from entries.models import EntryModel
from entries.api.serializers import EntrySerializer
from django.shortcuts import get_object_or_404
class EntryListAPI(APIView):
    def get(self, request):
        entries = EntryModel.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)
       
    def post(self, request):
        serializer = EntrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201 )
        
        return Response(status=400, data=serializer.errors)


class EntryListAPIid(APIView):        

    def get_entry(self, request, pk):
        entry= get_object_or_404(EntryModel, pk=pk)
           
        return entry

    def get(self, request, pk):
        entry= self.get_entry(request, pk)

        serializer= EntrySerializer(instance=entry)
        return Response(serializer.data)
        
    def put(self, request, pk):
        entry= get_object_or_404(EntryModel, pk)
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            entry.save()
            return Response(status = 400, data=serializer.errors)

    def delete(self, request, pk):
        entry= get_object_or_404(EntryModel, pk=pk)
        entry.delete()
        return Response(status=204)