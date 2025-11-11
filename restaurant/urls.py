from django.urls import path
from restaurant.views import Bookingview,MenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', MenuView.as_view(),
    path('booking/', Bookingview.as_view()))
]