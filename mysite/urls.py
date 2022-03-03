from django.conf.urls import include
from django.contrib import admin
from django.urls import path

admin.site.site_header="Colussus Clothing Admin"
admin.site.site_title="Colussus Clothing"
admin.site.index_title="Colussus Clothing"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
