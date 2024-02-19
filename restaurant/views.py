# from django.http import HttpResponse
from django.shortcuts import render
from .models import Booking, Menu
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class UserViewSet(viewsets.ModelViewSet):
#    permission_classes = [permissions.IsAuthenticated]
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer