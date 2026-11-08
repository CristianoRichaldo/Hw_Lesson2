from django.urls import path
from .views import AdminPanelAPIView, UserDashbroadAPIView

urlpatterns = [
    path('admin-panel/', AdminPanelAPIView.as_view(),name='admin-panel'),
    path('user-dashbroad/', UserDashbroadAPIView.as_view(),name='user-dashbroad'),
]