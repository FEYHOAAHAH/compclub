from django.shortcuts import render, redirect
from .forms import MyForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')
    else:
        form = MyForm()

    return render(request, 'index.html', {'form': form})


def show_success(request):
    return render(request, 'success.html')