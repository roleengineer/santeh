from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['Закажите услуги прямо сейчас по телефону или почте:', '0986816546', 'veritasreform@gmail.com']})
