from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from employer.forms import JobForm
from employer.models import Jobs
from django.urls import reverse_lazy

# Create your views here.
class EmployerHomeView(View):
    def get(self,request):
        return render(request,"emp-home.html")

class AddJobView(CreateView):
    model=Jobs
    form_class =JobForm
    template_name ="emp-addjob.html"
    success_url = reverse_lazy("emp-alljobs")

class ListJobView(ListView):
    model = Jobs
    template_name = "emp-listjob.html"
    context_object_name = "jobs"

class DetailJobView(DetailView):
    model=Jobs
    template_name = "emp-detailjob.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

class EditJobView(UpdateView):
    model=Jobs
    template_name = 'emp-editjob.html'
    form_class = JobForm
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"

class DeleteJobView(DeleteView):
    model=Jobs
    template_name = "jobconfirmdelete.html"
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"


#authentication section
from employer.forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    success_url = reverse_lazy("signin")
    template_name = "usersignup.html"

class SigninView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            psw=form.cleaned_data.get("password")
            user=authenticate(username=uname,password=psw)
            if user:
                login(request,user)
                return redirect("emp-home")
            else:
                return render(request,"login.html",{"form":form})
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "change-password.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("psw")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):
    template_name = "password-reset.html"
    def post(self, request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1 != pwd2:
            return render(request,self.template_name,{"msg":"Password mismatch"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")

