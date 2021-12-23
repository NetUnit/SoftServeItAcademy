'''
    The generic views provided by REST framework allow
    you to quickly build API views that map closely to
    your database models.

'''

from rest_framework import generics
from products.models import Product
from .serializers import ProductPostSerializer

class ProductCrudView(generics.RetrieveUpdateDestroyAPIView):
    '''
        Concrete view for the main CRUD operations:
        retrieving, updating or deleting a model instance.
        Shifts such classes as: DetailView, CreateView, UpdateView, Form View

    '''
    model = Product
    lookup_field = 'pk'
    serializer_class = ProductPostSerializer
    # queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            raise Http404('Object not found')
        return Product.objects.get(pk=pk) 


