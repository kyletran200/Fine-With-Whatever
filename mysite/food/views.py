from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import UserData
from rest_framework import viewsets
from django.views import generic
import requests
from .services import get_businesses, create_raw_business_list, chooseRandomBusiness
from django.conf import settings
# Create your views here.
API_HOST = "https://api.yelp.com/v3"
SEARCH_PATH = '/businesses/search'
all_businesses = []


def get_user_info(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_data = UserData()
            user_data.location = form.cleaned_data['your_location']
            user_data.search_radius = form.cleaned_data['your_search_radius']
            user_data.star_standard = form.cleaned_data['your_star_standard']
            user_data.save()
            return HttpResponseRedirect('/businesses/')
    else:
        form = UserForm()
    return render(request, 'userform.html', {'form': form})

class businessesPage(generic.TemplateView):

    model = UserData
    template_name = 'food/businessesPage.html'
    def get(self, request):
        show_businesses = []
        user_data = UserData.objects.last()
        location = user_data.location
        search_radius = user_data.search_radius
        star_standard = user_data.star_standard
        #create_final_business_list(all_businesses, location, search_radius, star_standard)
        all_businesses = create_raw_business_list(location, search_radius)
        place_to_eat = chooseRandomBusiness(all_businesses, star_standard)
        for i in range(len(all_businesses)):
            show_businesses.append(all_businesses[i]['name'])
        context = {
            'businesses_list': show_businesses,
            'place_to_eat': place_to_eat
        }
        return render(request, 'businessesPage.html', context)
