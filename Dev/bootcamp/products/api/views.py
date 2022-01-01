'''
    The generic views provided by REST framework allow
    you to quickly build API views that map closely to
    your database models.

'''

from rest_framework import generics, viewsets
from products.models import Product
from .serializers import ProductPostSerializer, TemporaryApiImageField
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import pathlib


class ProductCrudView(generics.RetrieveUpdateDestroyAPIView):
    '''
        Concrete view for the main CRUD operations:
        retrieving, updating or deleting a model instance.
        Shifts such classes as: DetailView, CreateView, UpdateView, Form View

    '''
    model = Product
    lookup_field = 'pk'
    serializer_class = ProductPostSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            raise Http404('Object not found')
        return Product.objects.get(pk=pk)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductPostSerializer
    queryset = Product.objects.all()
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    
    @action(detail=True, methods=['put', 'get', 'post'])
    def product(self, request, pk=None):
        ## 'image': [<InMemoryUploadedFile: creepy_bike_c641PhV.png (image/png)>]}
        # need to post/put this as an image in the raw data
        # print(request.data)
        try:
            product = get_object_or_404(self.queryset, pk=pk)
            api_data = request.data         
        
            json_raw_data = TemporaryApiImageField(product)

            data =  json_raw_data.to_internal_value(api_data)

            serializer = ProductPostSerializer(product, data=data)
            if not serializer.is_valid():
                print(False)
                return Response(serializer.errors)
            
            print('serializer is valid')
            serializer.save()
            return Response(serializer.data)
        except Exception as err:
            print(err)
            pass
    