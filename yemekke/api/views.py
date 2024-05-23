from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Store, Product, Order
from .serializers import UserSerializer, StoreSerializer, ProductSerializer, OrderSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

User = get_user_model()

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SellerCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SellerStoreCreate(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class SellerProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_seller and hasattr(user, 'store'):
            serializer.save(store=user.store)
        else:
            raise permissions.PermissionDenied("Only sellers with a store can create products.")

class SellerProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class UserTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]
