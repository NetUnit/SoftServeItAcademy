from rest_framework import generics
from manufacturer.models import Manufacturer
from .serializers import ManufacturerPostSerializer


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