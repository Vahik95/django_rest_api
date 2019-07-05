from django.conf.urls import url
from django.contrib import admin

from updates.views import JsonCBV, JsonCBV2, SerializedDetailView, SerializedListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
    url(r'^json/serialized_detail/$', SerializedDetailView.as_view()),
    url(r'^json/serialized_list/$', SerializedListView.as_view()),
]
