from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodosListApiViews.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosListGenericApiView.as_view()),
    path('generics/<pk>', views.TodosDetailGenericApiView.as_view(),)
]