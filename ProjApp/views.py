from django.contrib.auth.decorators import permission_required
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, FormView, CreateView, DeleteView, DetailView, UpdateView


from django.contrib.auth.mixins import LoginRequiredMixin
from ProjApp.forms import CustomPermissionForm, UploadForm
from ProjAppAuth.forms import UpdateSingleUserForm
from ProjApp.models import Source
from ProjAppAuth.models import User
from django.db.models import Count

# custom
from .customUserTest import *
from ProjAppAuth.models import CustomPermission


class IndexView(LoginRequiredMixin, ListView):
    template_name = "formain/in-nav.html"
    model = Source
    login_url = "login"
    context_object_name = "showAllDetails"


class PersonalDetails(LoginRequiredMixin, ListView):
    template_name = 'formain/your-details.html'
    model = User
    login_url = 'login'
    context_object_name = "personalDetails"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["personalDetails"] = Source.objects.filter(
            username=self.request.user.id)

        context["totalPost"] = Source.objects.all().count()
        context["newPost"] = Source.objects.all().order_by(
            'created_at').count()
        context["showOnlyUser"] = Source.objects.filter(
            username=self.request.user)
        context["totalUser"] = User.objects.all().count()
        return context

# crud


class UploadDetails(LoginRequiredMixin, FormView):
    template_name = "formain/addDetails.html"
    success_url = reverse_lazy("index")
    form_class = UploadForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.save()
        return super().form_valid(form)


class UpdateDetails(AdminAndModeratorCanEdit, UpdateView):
    template_name = "formain/edit-details.html"
    model = Source
    login_url = "login"
    success_url = reverse_lazy("data")
    form_class = UploadForm
# views.py


class DeleteDetails(AdminAndModeratorCanDelete, DeleteView):
    template_name = "formain/confirm-delete.html"
    success_url = reverse_lazy("data")
    context_object_name = "deletedata"
    model = Source
    login_url = "login"


@csrf_exempt
def update_total_hits(request):
    if request.method == "GET":
        source_id = request.GET.get("source_id")
        link = request.GET.get("link")

        source = Source.objects.get(pk=source_id)
        source.total_hits += 1
        source.save()

        data = {
            "total_hits": source.total_hits,
        }

        return JsonResponse(data)


class DataTable(LoginRequiredMixin, ListView):
    template_name = "formain/data.html"
    model = Source
    login_url = "login"
    context_object_name = "showAllDetails"


class UserDetails(AdminCanSeePages, ListView):
    model = User
    template_name = "formain/user-details.html"
    context_object_name = "userDetails"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userDetails"] = User.objects.annotate(
            countofpost=Count("source"))
        return context


class UpdateSingleUserData(AdminCanSeePages, UpdateView):
    form_class = UpdateSingleUserForm
    model = User
    login_url = "login"
    success_url = reverse_lazy("user-details")
    template_name = "formain/singleUserDetail.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        getID = self.kwargs.get("pk")
        user = User.objects.get(id=getID)
        context["showAllDetails"] = Source.objects.filter(
            username=user)
        return context


class CustomPermissionView(AdminCanSeePages, FormView):
    template_name = "formain/singleUserDetail.html"
    form_class = CustomPermissionForm
    model = User
    success_url = reverse_lazy("user-details")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@csrf_exempt
def rate_data(request):
    db = Source.objects.all()
    if request.method == 'POST':
        source_id = request.POST.get('source_id')
        rating = request.POST.get('rating')

        # Update the ratings for the source
        source = Source.objects.get(pk=source_id)
        source.ratings += int(rating)
        source.total_ratings += 1
        source.total_rating_count += 1
        source.save()

        average_rating = source.ratings / source.total_rating_count

        return JsonResponse({'average_rating': average_rating, 'total_ratings': source.total_ratings})
    return render(request, "formain/data.html", {"showAllDetails": db})


@permission_required('source.add_source')
def dummy(req):
    dbName = User.objects.all()
    return render(req, "formain/dummy.html")


class ManageUserPermissions(AdminCanSeePages, UpdateView):
    template_name = 'formain/singleUserDetail.html'
    form_class = CustomPermissionForm
    model = CustomPermission
    success_url = reverse_lazy("user-details")

    def form_valid(self, form):
        getId = self.kwargs["pk"]
        custom_permission, created = CustomPermission.objects.get_or_create(
            userName=getId)
        custom_permission.save()
        form.save()
        return super().form_valid(form)


class UpdateYourDetail(LoginRequiredMixin, UpdateView):
    fields = ["username", "email"]
    model = User
    success_url = reverse_lazy("personal-detail")
    template_name = "formain/edit-details.html"

    def get_object(self, **kwargs):
        token = self.kwargs.get("uuid")
        user = get_object_or_404(User, uuid=token)
        return user
