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
from django.db.models import Q
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
    )

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
    parser_classes = (
        JSONParser, FormParser,
        MultiPartParser, FileUploadParser
        )

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
    lookup_field = 'pk'
    serializer_class =  ManufacturerCreateSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (
        JSONParser, FormParser,
        MultiPartParser, FileUploadParser
        )
    
    def get_queryset(self):
        qs = Manufacturer.objects.all()
        query = self.request.GET.get('q')
        # return qs
        print(query)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            ).distinct()
        return qs

    def get_object(self):
        '''
            Shorter alternative of the method above
            :returns: self.obj searched via title
        '''
        pk = self.kwargs.get('pk')
        print(pk)
        data = self.request.data
        print(data)
        title = data.get('title')
        if not title:
            raise serializers.ValidationError({
                'detail': 'Title wasn\'t selected [ ± _ ± ]',
                })
        obj = Manufacturer.objects.filter(title=title).get()
        return obj
        
    def check_permissions(self, request=None):
        '''
            Check permission to create/look for objects
            :returns: True when user pass the permission is_authenticated()
        '''
        permission = IsOwnerOrReadOnly()
        view = self.get_view_name()
        request = self.request
        permission_to_create = permission.has_permission(request, view)
        permission_need = request.method in ['PUT', 'POST', 'PATCH'] # not in permissions.SAFE_METHODS
        if not permission_to_create and permission_need:
            raise NotAuthenticated(_('This is allowed for authenticated users only ( ´･･)ﾉ(._.`)'))
        return True

    def check_object_permissions(self, request=None, obj=None):
        '''
            Check permission to adjust object PUT/PATCH Methods
            :returns: True when user pass the permission (is author of an object)
        '''
        permission = IsOwnerOrReadOnly()
        view = self.get_view_name()
        request = self.request
        obj = self.get_object()
        permission_to_adjust = permission.has_object_permission(request, view, obj)
        if not permission_to_adjust:
            raise PermissionDenied(_('This is allowed for the owner only  (」＞＜)」'))
        return True
        
    def check_auth_and_blocked(self):
        '''
            Check if user isn't in the Blocklist
            :returns: True when user isnt blocked
        '''
        permission =  BlocklistPermission()
        view = self.get_view_name()
        request = self.request
        permission = permission.has_permission(request, view)
        if not permission:
            raise PermissionDenied(_(
            'U don\'t have permission to access: ' + 
            self.request.META.get('REMOTE_ADDR'))
            )
        return True

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         raise Http404('Manufacturer wasn\'t found')
    #     return Manufacturer.objects.get(pk=pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # print(serializer, 'This is serialiazer')
        serializer.save()
    
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