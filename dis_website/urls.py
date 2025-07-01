
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('account/',include("account.urls")),
    path('dashboards/',include("dashboard.urls")),
    path('api/core/', include('core.urls')),
    path('api/people/', include('people.urls')),
    path('api/enrollment/', include('enrollment.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/results/', include('results.urls')),
]


