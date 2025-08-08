
from django.urls import path
from .views import *

urlpatterns = [
    path('insert-student/', StudentInsertView.as_view(), name='insert_student'),
    path('get-student/', StudentGetView.as_view(), name='get_student'),
    path('get-all-students/', StudentGetAllView.as_view(), name='get_all_students'),
    path('delete-one-student/', StudentDeleteView.as_view(), name='delete_one_student'),
    path("update-student/", StudentInsertView.as_view(), name='update_student'),  # Reusing insert view for update
    path('add-two-numbers/', TaskforRachana.as_view(), name='add_two_numbers'),
    path("demo-work/",sakshidemoview.as_view(), name='demo_view')
    #add urls as per your requirement
    path('anushka-task/', TaskforAnushka.as_view(), name='anushka-task'),

] 
