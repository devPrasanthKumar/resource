from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages


class AdminCanSeePages(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "login"

    def test_func(self):
        return self.request.user.userMode == "admin"

    def handle_no_permission(self):
        messages.error(
            self.request, "You dont have  permission , thats why you have redirect here")
        return redirect("index")


class BothCanSeePages(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "login"

    def test_func(self):
        return self.request.user.userMode == "admin" or self.request.user.userMode == "moderator"

    def handle_no_permission(self):
        messages.error(
            self.request, "You dont have  permission , thats why you have redirect here")
        return redirect("index")


class AdminAndModeratorCanDelete(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "login"

    def test_func(self):
        return self.request.user.userMode == "admin" or self.request.userMode == "moderator" and self.request.user.custompermission.can_delete

    def handle_no_permission(self):
        messages.error(
            self.request, "You dont have  permission to access it")
        return redirect("index")


class AdminAndModeratorCanEdit(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "login"

    def test_func(self):
        return self.request.user.userMode == "admin" or self.request.userMode == "moderator" and self.request.user.custompermission.can_edit

    def handle_no_permission(self):
        messages.error(
            self.request, "You dont have  permission to access it")
        return redirect("index")
