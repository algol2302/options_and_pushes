from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PushForm, Options


@login_required
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PushForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PushForm()

    return render(request, "index.html", {"form": form})


@login_required
def options(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Options(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = Options()

    return render(request, "index.html", {"form": form})
