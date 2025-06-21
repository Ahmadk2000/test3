from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ✅ استيراد عرض الصفحة الرئيسية من products
from products.views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # ✅ عرض الصفحة الرئيسية عند /
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]

# ✅ دعم ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
