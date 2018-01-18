from django.conf.urls import url
from . import views

app_name = 'order'
urlpatterns = [
    url(r'^create/',views.order_create,name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$',views.admin_order_pdf,name='admin_order_pdf'),
    url(r'^admin/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),
]