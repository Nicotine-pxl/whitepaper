from django.contrib import admin
from django.urls import path
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_view, name='contact'),
]
