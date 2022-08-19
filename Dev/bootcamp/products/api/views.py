'''
Generic views provided by REST framework allow
you to quickly build API views that map closely to
our database models.
'''

from rest_framework import generics, viewsets, mixins
from products.models import Product
from .serializers import (
    ProductPostSerializer,
    TemporaryApiImageData,
    ProductCreateSerializer,
)
from rest_framework.decorators import action
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
    JSONParser,
    FileUploadParser
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# path
import pathlib
from bootcamp.settings import MEDIA_ROOT
from pathlib import Path
import os

from django.core.exceptions import ValidationError
from django.http.response import Http404
from django.utils.translation import gettext as _
from rest_framework import serializers

from django.db.models import Q

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from bootcamp.api.permissions import (
    IsOwnerOrReadOnly,
    BlocklistPermission
)

from rest_framework.exceptions import (
    PermissionDenied,
    NotAuthenticated,
)


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
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]

    @action(detail=True, methods=['put', 'get', 'post', 'patch'])
    def product(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        api_data = request.data

        # get full data
        full_data = request.__dict__.get('_full_data')
        title = full_data.get('title')

        json_raw_data = TemporaryApiImageData(product)
        data = json_raw_data.save(api_data)

        # update a raw with partial data partial=True
        # avoid error of title as required field
        serializer = ProductPostSerializer(product, data=data, partial=True)
        serializer.validate_title(title)

        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class ProductAPIView(generics.CreateAPIView):
    model = Product
    lookup_field = 'pk'
    serializer_class = ProductCreateSerializer
    parser_classes = (
        JSONParser,
        FormParser,
        MultiPartParser,
        FileUploadParser)
    permission_classes = [AllowAny]
    # queryset = Product.objects.all()

    def get_queryset(self):
        '''
        Overrrides self-attr 'queryset'
        :returns: existing models queryset
        '''
        return Product.objects.all()

    def perform_create(self, serializer):
        api_data = self.request.data
        image = api_data.get("image")
        user = self.request.user
        serializer.save(user=self.request.user, image=image)


class ProductMixinAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          generics.ListAPIView):
    '''
        ==================================================================
        This class represents ListApiView along with create/update ability
        ==================================================================
        Attrs:
        :param name: Describes the comapny name
        :type name: str max_length = 40
        :param country: Depicts the manufacturer's country of origin
        :type country: str max_length = 20
        :param year: depicts the foundation year year of a company
        :type date: datetime.date

        .. note::
            permission_classes:
            IsAuthenticated - requires auth to any of methods
            IsAuthenticatedOrReadOnly - allows to implement GET method without auth
            IsOwnerOrReadOnly - allows to update objects only for owners
            ReadOnly - allows to apply only SAFE_METHODS ('GET', 'HEAD', 'OPTIONS')
            Destroy mixin requires pk, that's why werent added.
            If we do not supply pk to delete, the operation fails.
            https://stackoverflow.com/questions/61833947/django-mixins-
            destroymodelmixin-delete-method-not-allowed
    '''

    model = Product
    lookup_field = 'pk'
    serializer_class = ProductCreateSerializer
    parser_classes = (
        JSONParser, FormParser,
        MultiPartParser, FileUploadParser
    )

    permission_classes = [
        IsAuthenticated,
        # IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
        # AllowAny
    ]

    # defines existing models queryset
    # queryset = Product.objects.all()

    def _allowed_methods(self):
        methods = [
            m.upper() for m in self.http_method_names if hasattr(self, m)
        ]
        methods.append('DELETE')
        return methods

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get('q')
        # print(qs)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).distinct()
        return qs

    def get_object(self, *args, **kwargs):
        '''
        Allows to add PUT/PATCH methods
        get_object - method that redefines self.object
        & allows to change the next without search via
        lookup_filed (if such doesn\'t exists)

        based on answer:
        https://stackoverflow.com/questions/43859053/django-rest-framework-
        assertionerror-fix-your-url-conf-or-set-the-lookup-fi/43859898#43859898

        :returns: self.obj searched via title
        '''

        data = self.request.data
        title = data.get('title')
        if not title:
            raise serializers.ValidationError({
                'detail': 'Title wasn\'t selected [ ± _ ± ]',
            })
        qs = Product.objects.filter(title=title)
        if qs.exists():
            obj = qs.get()
            return obj
        raise Http404()

    # def get_object(self):
    #     '''
    #     Shorter alternative of the method above
    #     :returns: self.obj searched via title
    #     '''
    #     data = self.request.data
    #     title = data.get('title')
    #     obj = get_object_or_404(Product, title=title)
    #     return obj

    def check_permissions(self, request=None):
        permission = IsOwnerOrReadOnly()
        view = self.get_view_name()
        request = self.request
        permission_to_create = permission.has_permission(request, view)
        permission_need = request.method in ['PUT', 'POST', 'PATCH', 'DELETE']
        if not permission_to_create and permission_need:
            raise NotAuthenticated(
                _('This is allowed for authenticated users only ( ´･･)ﾉ(._.`)')
            )
        return True

    def check_object_permissions(self, request=None, obj=None):
        '''
        Only owners check. Allow owners of a product to edit it.
        :returns: True when user pass the permission (is author of an object)
        '''
        permission = IsOwnerOrReadOnly()
        view = self.get_view_name()
        request = self.request
        obj = self.get_object()
        permission_to_adjust = permission.has_object_permission(
            request, view, obj)
        if not permission_to_adjust:
            raise PermissionDenied(
                _('This is allowed for the owner only  (」＞＜)」'))
        return True

    def check_auth_and_blocked(self):
        '''
        Check if user isn't in the Blocklist
        :returns: True when user isnt blocked
        '''
        permission = BlocklistPermission()
        view = self.get_view_name()
        request = self.request
        permission = permission.has_permission(request, view)
        if not permission:
            raise PermissionDenied(_('U don\'t have permission to access: ' +
                                   self.request.META.get('REMOTE_ADDR')))
        return True

    def perform_update(self, serializer):
        serializer.save()
        # serializer.save(commit=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    def post(self, request, *args, **kwargs):
        '''
        Add POST method to "Allow" list of HTTP methods:
        :returns: new product object created
        '''
        self.check_permissions()
        obj = self.create(request, *args, **kwargs)
        return obj

    def put(self, request, *args, **kwargs):
        '''
        Add PUT method to "Allow" list of HTTP methods:
        :returns: new product object updated
        '''
        self.check_object_permissions()
        obj = self.update(request, *args, **kwargs)
        return obj

    def patch(self, request, *args, **kwargs):
        '''
        Add PUT method to "Allow" list of HTTP  methods:
        :returns: new product object updated
        '''
        self.check_object_permissions()
        obj = self.partial_update(request, *args, **kwargs)
        return obj

    def get_inherited_methods(self):
        '''
        :returns: * parent methods & attrs
        '''
        return print(dir(self))
