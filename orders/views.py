from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import Order



# Create your views here.
def index(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)


class userFormView(View):
    form_class = UserForm
    template_name = 'orders/register.html'
    
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
                    return redirect('orders:index')
                
        context = {
            "form": form,
        }
        return render(request, 'orders/register.html', context) 