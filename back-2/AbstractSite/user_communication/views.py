from imp import reload
from multiprocessing import context
from telnetlib import STATUS
from webbrowser import get
from django.shortcuts import redirect, render
from .forms import *
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.loader import render_to_string

def account(request):
    reg_form = UserReg()
    log_form = UserLog()
    return render(request=request, template_name='account/account.html', context={'reg_form':reg_form, 'log_form':log_form})

def logout(request):
    auth.logout(request)
    return redirect('account')

class Index(ListView):
    paginate_by = 4
    model = CustomUser
    template_name = "main/index.html"
    context_object_name = "users"

    def get_queryset(self):
        if "username" in self.request.GET:
            username = self.request.GET.get("username")
            return CustomUser.objects.filter(Q(first_name__icontains=username) | Q(last_name__icontains=username))
        else:
            return CustomUser.objects.all()
    
class Lab(ListView):
    model = Figure
    template_name = "main/lab.html"
    context_object_name = "figures"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MakeFigure()
        return context
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return user.figure_set.all().order_by('-id').select_related('type')
        else:
            return redirect('home') 

class User(View):  
    def get(self, request, *args, **kwargs):
        if "figure" in request.GET:
            user_recipent = CustomUser.objects.get(username=request.GET.get("username_recipent"))
            user_current = request.user
            figure = Figure.objects.get(slug=request.GET.get("figure"))
            if "like" in request.GET:
                if user_recipent == user_current:
                    return JsonResponse({"error":"You can`t like yourself"}, status = 202)
                else:
                    if not FigureLike.objects.filter(user=user_current, figure=figure).exists():
                        FigureLike.objects.create_like(figure=figure, user=user_current)
                        return JsonResponse({"likes":figure.likes, "figure":figure.pk}, status = 200)
                    else:
                        like = FigureLike.objects.get(user=user_current, figure=figure)
                        FigureLike.objects.delete_like(figure=figure, user=user_current)
                        figure.save()
                        return JsonResponse({"likes":figure.likes, "figure":figure.pk}, status = 200)
            else:
                if user_recipent == user_current:
                    return JsonResponse({"error":"You can`t give F to yourself"}, status = 202)
                else:
                    if not FigureBlacklist.objects.filter(user=user_current, figure=figure).exists():
                        if user_current.money >= figure.cost:
                            if user_recipent.money + figure.cost <= 99999999:
                                user_recipent.money += figure.cost
                                user_recipent.save()
                                FigureBlacklist.objects.create(user=user_current, figure=figure)
                                return JsonResponse({"cost":user_recipent.money}, status = 200)
                            else:
                                FigureBlacklist.objects.create(user=user_current, figure=figure)
                                return JsonResponse({"cost":user_recipent.money}, status = 200)
                        else:
                            return JsonResponse({"error":"You have so few F"}, status = 202)
                    else:
                        return JsonResponse({"error":"You already give F to this figure"}, status = 202)
        else:
            context = {}
            user = CustomUser.objects.get(username=kwargs["username_slug"])
            context["user_info"] = user
            context["works"] = len(user.figure_set.all())
            context["figures"] = user.figure_set.all().select_related('type')
            return render(request=request, template_name="main/user_page.html", context=context)

class Account(View):
    form_class = UserReg
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if self.form_class == UserReg:
            if form.is_valid():
                form.save()
                return JsonResponse({"success_link":reverse_lazy('account')}, status = 200)
            else:
                return JsonResponse({"error":form.errors}, status = 202)
        elif self.form_class == UserLog:
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return JsonResponse({"success_link":reverse_lazy('home')}, status = 200)
            else:
                return JsonResponse({"invalid_account":"You data dont exists in DB"}, status = 202)

class CreateFigure(View):
    form_class = MakeFigure
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            figure = form.save(commit=False)
            figure.user = request.user
            figure.save()
            context = {"figure":figure}
            html = render_to_string('small/figure.html', context=context)
            return JsonResponse({"html":html}, status=200)
        else:
            return JsonResponse({"error":form.errors}, status = 202)