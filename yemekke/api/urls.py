from django.urls import path
from .views import (
    UserCreate,
    SellerCreate,
    SellerStoreCreate,
    SellerProductCreate,
    SellerProductList,
    OrderCreate,
    OrderList,
    UserTokenObtainPairView,
    UserTokenRefreshView
)

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('sellers/', SellerCreate.as_view(), name='seller-create'),
    path('sellers/stores/', SellerStoreCreate.as_view(), name='store-create'),
    path('sellers/products/', SellerProductCreate.as_view(), name='product-create'),
    path('sellers/products/list/', SellerProductList.as_view(), name='product-list'),
    path('orders/', OrderCreate.as_view(), name='order-create'),
    path('orders/list/', OrderList.as_view(), name='order-list'),
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
]
