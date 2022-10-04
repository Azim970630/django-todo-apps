from django.urls import path
from .views import CustomLogoutView, CustomLoginView, RegisterPage, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks-lists'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks-details'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>', TaskUpdate.as_view(), name='task-edit'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete')
]