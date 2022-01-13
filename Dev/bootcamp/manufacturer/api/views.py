from rest_framework import generics, mixins, serializers
from manufacturer.models import Manufacturer
from .serializers import (
    ManufacturerPostSerializer,
    ManufacturerCreateSerializer
    )

from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
    JSONParser, 
    FileUploadParser
    )

from django.shortcuts import get_object_or_404

class ManufacturerCrudView(generics.RetrieveUpdateDestroyAPIView):
    '''
        Concrete view for the main CRUD operations:
        retrieving, updating or deleting a model instance.
        Shifts such classes as: DetailView, CreateView, UpdateView, Form View
    '''
    model = Manufacturer
    lookup_field = 'pk'
    serializer_class = ManufacturerPostSerializer

    def get_queryset(self):
        return Manufacturer.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            raise Http404('Manufacturer not found')
        return Manufacturer.objects.get(pk=pk)

class ManufacturerCreateAPIView(generics.CreateAPIView):
    '''
        Manufacturer API View
    '''
    model = Manufacturer
    lookup_field = 'pk'
    serializer_class =  ManufacturerCreateSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)

    def get_queryset(self):
        ''' 
            Overrrides self-attr 'queryset'
            :returns: existing models queryset
        '''
        return Manufacturer.objects.all()

    def perform_create(self, serializer):
        api_data = self.request.data
        image = api_data.get("image")
        serializer.save(image=image)

class ManufacturerMixinAPIView(mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                generics.ListAPIView):
    model = Manufacturer
    lookup_field = 'title'
    serializer_class =  ManufacturerCreateSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)
    
    # defines existing models queryset
    queryset = Manufacturer.objects.all()

    def get_object(self):
        '''
            Shorter alternative of the method above
            :returns: self.obj searched via title
        '''
        data = self.request.data
        title = data.get('title')
        print(title)
        if not title:
            raise serializers.ValidationError({
                'detail': 'Title wasn\'t selected [ ± _ ± ]',
                })
        obj = Manufacturer.objects.filter(title=title).get()
        return obj
        
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         raise Http404('Manufacturer wasn\'t found')
    #     return Manufacturer.objects.get(pk=pk)

    def post(self, request, *args, **kwargs):
        ''' 
            Add POST method to "Allow" list of HTTP  methods:
            :returns: new manufacturer object created 
        '''
        obj = self.create(request, *args, **kwargs)
        return obj
    
    # def perform_update(self, serializer):
    #     print(serializer)
    #     api_data = self.request.data
    #     print(api_data)
    #     serializer.save(commit=False)


    def put(self, request, *args, **kwargs):
        ''' 
            Add PUT method to "Allow" list of HTTP  methods:
            :returns: updated manufacturer object 
        '''
        obj = self.update(request, *args, **kwargs)
        return obj

    def patch(self, request, *args, **kwargs):
        ''' 
            Add PATCH method to "Allow" list of HTTP  methods:
            :returns: updated manufacturer object  
        '''
        obj = self.update(request, *args, **kwargs)
        return obj 
        
    def get_inherited_methods(self):
        '''
            Will return * parent methods & attrs
        '''
        return print(dir(self))

# "media/manufacturers/c69d6a2f-27f.png"