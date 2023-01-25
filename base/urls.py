from django.urls import include, path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, loginPage, registerPage,logOutUser,DeadlineSort,CompleteSort,NameSort
# from views import *


urlpatterns = [
    path('', loginPage),
    path('task-list/', TaskList.as_view(), name='tasks'),
    path('login/', loginPage, name='login'),
    path('logout/', logOutUser, name='logout'),
    path('deadline-sort/', DeadlineSort.as_view(), name='deadline-sort'),
    path('complete-sort/', CompleteSort.as_view(), name='complete-sort'),
    path('name-sort/', NameSort.as_view(), name='name-sort'),
    path('register/', registerPage, name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),

]
