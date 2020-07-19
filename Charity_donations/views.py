from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from Charity_donations.models import Donation, Institution


# Create your views here.
class LandingPage(View):
    def get(self, request):
        helped_ins_num = Institution.objects
        bags_num = Donation.objects.aggregate(sum=Sum('quantity'))['sum']
        institution_num = helped_ins_num.count()
        return render(request, 'index.html',
                      {'bags': bags_num, 'institutions': institution_num})


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
