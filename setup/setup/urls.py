"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from auth import urls as authModule
from users import urls as userModule
from drug import urls as drugModule
from dispensing import urls as dispensingModule
from stock import urls as stockModule
from storerequest import urls as orderModule
from supplier import urls as supplierModule
from purchaseorder import urls as purchaseorderModule
from storetransfer import urls as storetransferModule
from userstore import urls as userstoreModule
from store import urls as storeModule

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(authModule)),
    path('api/user/', include(userModule)),
    path('api/drug/', include(drugModule)),
    path('api/dispensing/', include(dispensingModule)), 
    path('api/stock/', include(stockModule)),
    path('api/order/', include(orderModule)),
    path('api/supplier/', include(supplierModule)),
    path('api/storetransfer/', include(storetransferModule)),
    path('api/purchaseorder/', include(purchaseorderModule)),
    path('api/userstore/', include(userstoreModule)),
    path('api/store/', include(storeModule)),
]
