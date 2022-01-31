from django.urls import path
from libraryApp import views
from .forms import LoginForm,CheckoutForm
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart,ItemDetailView,PaymentView,CheckoutView,OrderSummaryView,remove_single_item_from_cart,remove_from_cart
from django.contrib.auth import views as auth_views

app_name = 'libraryApp'

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('account/login/',auth_views.LoginView.as_view(template_name="libraryApp/login.html",authentication_form=LoginForm),name='login'),
    path('signup/', views.UserRegistrationView.as_view(),name='signup'),
    path('order-summary/',views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<title>/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('productdetail/<title>/<int:pk>/', ItemDetailView.as_view(), name='productdetail'),
    path('remove-from-cart/<title>/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<title>/<int:pk>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
"""path('Passwordchange/',auth_views.LoginView.as_view(template_name="libraryApp/Passwordchange.html",form_class=PasswordchangeForm),name='Passwordchange'),"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
