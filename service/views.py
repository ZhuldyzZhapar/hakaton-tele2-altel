from django.shortcuts import render, get_object_or_404, redirect
from .forms import IdentificationForm
from .models import Identification
from service.src.face_verification import face_verification
import time
from django.db import connection
# Create your views here.

'''def index(request):
	customers = Identification.objects.all()
	print(customers)
	print(connection.queries)
	return render(request, 'index.html', {})
'''


def identification_result(request, pk):
	customer = get_object_or_404(Identification, pk=pk)
	face_verified = face_verification()   #(customer.id_card_img, customer.selfie_img)
	return render(request, 'identification_result.html', {'customer': customer, 'face_verified': face_verified })


def index(request):
	if request.method == 'POST':
		form = IdentificationForm(request.POST, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('identification_result', pk=post.id)
	else:
		form = IdentificationForm()
	return render(request, 'index.html', {'form': form})


def delete(request, pk):
	del_cust = Identification.objects.get(id=pk)
	del_cust.delete()
	return redirect('/')