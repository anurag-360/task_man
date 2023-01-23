from django.urls import include, path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, loginPage, registerPage,logOutUser,deadlineSort
# from views import *


urlpatterns = [
    path('', loginPage),
    path('task-list/', TaskList.as_view(), name='tasks'),
    path('login/', loginPage, name='login'),
    path('logout/', logOutUser, name='logout'),
    path('deadline-sort/', deadlineSort, name='deadline-sort'),
    path('register/', registerPage, name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),

]
