from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List


@login_required
def list_index(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            List.objects.create(
                user=request.user,
                title=title
            )
        return redirect("lists/list_index")
    lists = (List.objects.filter(user=request.user).order_by("-updated_at"))
    return render(request, "lists/index.html", {"lists": lists})