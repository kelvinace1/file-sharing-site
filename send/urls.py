from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import Home, FileView, FileDetail, FileCreate, UserFileView, FileUpdate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('files/', FileView.as_view(), name='files'),
    path('my_files/', UserFileView.as_view(), name='user_files'),
    path('<uuid:pk>/', FileDetail.as_view(), name='file_detail'),
    path('add/', FileCreate.as_view(), name='file_create'),
    path('update/<uuid:pk>/', FileUpdate.as_view(), name='file_update'),
]