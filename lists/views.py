from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List


@login_required
def list_index(request):
    lists = (List.objects.filter(user=request.user).order_by("-updated_at"))
    return render(request, "lists/index.html", {"lists": lists})