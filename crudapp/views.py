from django.shortcuts import render, redirect
from .models import News

# Create your views here.

def index(request):
    records = News.objects.all()

    context = {
        'records' : records
    }
    return render(request, 'index.html', context)


def Add(request):
    if request.method == 'POST':
        news_title = request.POST.get('news_title')
        news_description = request.POST.get('news_description')
        news_banner_image = request.POST.get('news_banner_image')
        category = request.POST.get('category')
        region = request.POST.get('region')
        status = request.POST.get('status')
        language = request.POST.get('language')
        city = request.POST.get('city')
        country = request.POST.get('country')
        createdby = request.POST.get('createdby')

        add_records = News(
            news_title = news_title,
            news_description = news_description,
            news_banner_image = news_banner_image,
            category = category,
            region = region,
            status = status,
            language = language,
            city = city,
            country = country,
            createdby = createdby
        )
        add_records.save()
        return redirect('home')

    return render(request, 'index.html')

def Edit(request):
    edit_records = News.objects.all()
    context = {
        'edit_records': edit_records
    }
    return redirect(request, 'index.html', context)


def Update(request, id):
    if request.method == 'POST':
        news_title = request.POST.get('news_title')
        news_description = request.POST.get('news_description')
        news_banner_image = request.POST.get('news_banner_image')
        category = request.POST.get('category')
        region = request.POST.get('region')
        status = request.POST.get('status')
        language = request.POST.get('language')
        city = request.POST.get('city')
        country = request.POST.get('country')
        createdby = request.POST.get('createdby')

        add_records = News(
            id = id,
            news_title = news_title,
            news_description = news_description,
            news_banner_image = news_banner_image,
            category = category,
            region = region,
            status = status,
            language = language,
            city = city,
            country = country,
            createdby = createdby
        )
        add_records.save()
        return redirect('home')

    return redirect(request, 'index.html')


def Delete(request, id):
    delete_records = News.objects.filter(id = id)
    delete_records.delete()
    context = {
        'delete_records':delete_records
    }
    return redirect('home') 