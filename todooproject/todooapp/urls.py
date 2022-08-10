from .import views
from django.urls import path

urlpatterns = [
        path('',views.add,name='add'),
        path('delete/<int:taskid>/',views.delete,name='delete'),
        path('update/<int:id>/',views.update,name='update'),
        path('ctvhome/',views.Tasklistview.as_view(),name='ctvhome'),
        path('ctvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='ctvdetail'),
        path('ctvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='ctvupdate'),
        path('ctvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='ctvdelete'),
]