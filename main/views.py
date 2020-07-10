import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import commentForm
from main.models import comment
from django.views.generic import ListView


# Create your views here.


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def add_comment(request):
    form = commentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return (render(request, "main/add_comment.html", {"form": form}))


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = comment

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
