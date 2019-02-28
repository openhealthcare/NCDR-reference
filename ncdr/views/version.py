from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, RedirectView, View

from ..models import Version


class SwitchToLatestVersion(LoginRequiredMixin, RedirectView):
    """Switch to the given version for the current user."""

    def get(self, request, *args, **kwargs):
        request.user.switch_to_latest_version()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return self.request.GET.get("next", reverse("index_view"))


class SwitchToVersion(LoginRequiredMixin, RedirectView):
    """Switch to the given version for the current user."""

    def get(self, request, *args, **kwargs):
        try:
            version = Version.objects.get(pk=self.kwargs["pk"])
        except Version.DoesNotExist:
            raise Http404

        request.user.switch_to_version(version)

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return self.request.GET.get("next", reverse("index_view"))


class PublishVersion(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        try:
            version = Version.objects.get(pk=self.kwargs["pk"])
        except Version.DoesNotExist:
            raise Http404

        version.is_published = True
        version.save()

        messages.success(request, f"Version {version.pk} has been published")

        return redirect(request.GET.get("next", reverse("index_view")))


class UnPublishVersion(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        try:
            version = Version.objects.get(pk=self.kwargs["pk"])
        except Version.DoesNotExist:
            raise Http404

        version.is_published = False
        version.save()

        messages.success(request, f"Version {version.pk} has been unpublished")

        return redirect(request.GET.get("next", reverse("index_view")))


class VersionList(LoginRequiredMixin, ListView):
    paginate_by = 50
    queryset = Version.objects.order_by("-pk", "-created_at")
    template_name = "version_list.html"