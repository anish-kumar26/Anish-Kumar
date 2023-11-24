# techiehub/urls.py

from django.urls import path
from .views import login, home, service, contact, about, loader, product_page, cart, buy, iphone
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import GmailView, product_page


urlpatterns = [
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('loader/', about, name='loader'),
    path('', home, name='home'),
    path('gmail/', GmailView.as_view(), name='gmail'),
    path('products/<str:product_type>/', product_page, name='product_page'),
    path('cart/', cart, name='cart'),
    path('buy/<int:product_id>/', buy, name='buy'),
    path('iphone/', iphone, name='iphone'),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)