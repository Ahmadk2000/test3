from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# عرض الصفحة الرئيسية
from products.views import home_view  # تأكد أن home_view موجود في products/views.py

urlpatterns = [
    path('', home_view, name='home'),  # هذا يعالج 404 عند زيارة /
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
