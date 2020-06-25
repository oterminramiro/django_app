from django.shortcuts import render, redirect

# Create your views here.
def main(request):
	context = {}
	return render(request, 'dashboard/main.html', context)
