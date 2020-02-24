from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm



class userFormView(View):
    form_class = UserForm
    template_name = 'users/register.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:

                    login(request, user)
                    return HttpResponseRedirect(reverse("orders:index"))
                
        context = {
            "form": form,
        }
        return render(request, 'users/register.html', context) 



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("orders:index"))

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("orders:index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "users/login.html", {"message": " "})        