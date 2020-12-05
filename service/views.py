from django.shortcuts import render, get_object_or_404, redirect
from .forms import IdentificationForm
from .models import Identification
# Create your views here.

def index(request):
	return render(request, 'index.html', {})


def identification_result(request, pk):
    customer = get_object_or_404(Identification, pk=pk)
    return render(request, 'identification_result.html', {'customer': customer})

def new_customer(request):
	if request.method == 'POST':
		form = IdentificationForm(request.POST, request.FILES or None)
		if form.is_valid():
			customer = form.save(commit = False)
			customer.author = request.user
			customer.save()

			return redirect('identification_result', pk=customer.pk)
	else:
		form = IdentificationForm()
	return render(request, 'index.html', {'form': form})