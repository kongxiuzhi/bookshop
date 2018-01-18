from django.conf.urls import url
from . import views

app_name="shop"
urlpatterns = [
    url(r'^$',views.indexView,name="index"),
    url(r'^list/(?P<categoryid>\d+)/$',views.indexView,name="book_list_by_category"),
    url(r'^detail/(?P<id>\d+)/$',views.book_detail,name="book_detail"),
]