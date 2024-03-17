from django.shortcuts import render, redirect, reverse
from .forms import AdvertisementForm
from .models import Advertisement

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'advert/advertisement_detail.html', {'advertisement': advertisement})

def create_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save()
            # Redirect to the advertisement detail page
            return redirect(reverse('advert:advertisement_detail', kwargs={'pk': advertisement.pk}))
    else:
        form = AdvertisementForm()
    # get tier chosen by user
    tier = request.GET.get('tier')
    return render(request, 'advert/create_advertisement.html', {'form': form, 'tier': tier})