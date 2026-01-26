from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List
from .forms import Listform


@login_required
def list_index(request):
    if request.method == "POST":
        form = Listform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("lists/list_index")
    else:
        form = Listform()
    lists = List.objects.filter(user=request.user).order_by("-updated_at")
    return render(request, "lists/index.html", {
        "form": form,
        "lists": lists,
    })