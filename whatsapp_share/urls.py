from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'whatsapp_share.views.home', name='home'),
    url(r'^items-list/$', 'whatsapp_share.views.items_list', name='item_list'),
    url(r'^items/$', 'whatsapp_share.views.items_create', name='item_create'),
    url(r'^orders/$', 'whatsapp_share.views.order_create', name='order_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
