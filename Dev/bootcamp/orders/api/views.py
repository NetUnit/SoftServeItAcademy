
from .serializers import OrderPostSerializer
from rest_framework import generics
from orders.models import Order


class OrderCrudView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Concrete view for the main CRUD operations:
    retrieving, updating or deleting a model instance.
    Shifts such classes as: DetailView, CreateView, UpdateView, Form View
    '''
    model = Order
    lookup_field = 'pk'
    serializer_class = OrderPostSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            raise Http404('Order not found')
        return Order.objects.get(pk=pk)
