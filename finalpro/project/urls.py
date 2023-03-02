from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('save_signupStud', views.save_signupStud, name='save_signupStud'),
    path('save_signupLect', views.save_signupLect, name='save_signupLect'),
    path('keyin', views.keyin, name='keyin'),
    path('search_class', views.search_class, name='search_class'),
    path('delete_student/<str:r_id_id>/', views.delete_student, name='delete_student'),
    path('delete_result/<str:r_id_id>/<str:r_code>/', views.delete_result, name='delete_result'),
    path('update_result/<str:r_id_id>/', views.update_result, name='update_result'),
    path('save_update_result/<str:r_id_id>/', views.save_update_result, name='save_update_result'),
    path('checking', views.checking, name='checking'),
    path('student_result/', views.student_result, name='student_result'),
    path('add_class', views.add_class, name='add_class'),
    path('view_class', views.view_class, name='view_class'),
    path('delete_class/<str:a_class>/', views.delete_class, name='delete_class'),
    path('update_class/<str:lecture>/', views.update_class, name='update_class'),
    path('save_update_class/<str:lecture>/', views.save_update_class, name='save_update_class'),
]

