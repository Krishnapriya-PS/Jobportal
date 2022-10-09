from django.urls import path
from employer import views
urlpatterns=[
    path('home',views.EmployerHomeView.as_view(),name="emp-home"),
    path('jobs/addjob',views.AddJobView.as_view(),name="emp-addjob"),
    path('jobs/alljobs',views.ListJobView.as_view(), name="emp-alljobs"),
    path('jobs/detail/<int:id>',views.DetailJobView.as_view(), name="emp-detailjob"),
    path('jobs/edit/<int:id>', views.EditJobView.as_view(), name="emp-editjob"),
    path('jobs/delete/<int:id>', views.DeleteJobView.as_view(), name="emp-deletejob"),
    path('users/accounts/signup',views.SignupView.as_view(),name="signup"),
    path('users/accounts/signin', views.SigninView.as_view(), name="signin"),
    path('users/accounts/signout', views.signout_view, name="signout"),

]