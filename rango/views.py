# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category, Page

def index(request) :
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'category_list' : category_list}
    return render_to_response('rango/index.html', context_dict, context)

def about(request) :
    return HttpResponse("Rango Says : here's its the about page!<br /><a href=\"/rango\">home</a>")

def category(request, category_name_url):
    context = RequestContext(request)

    category_name_url = category_name_url.replace('_', ' ')
    context_dict = {'category_name' : category_name_url}

    try:
        category = Category.objects.get(name = category_name_url)
        pages = Page.object.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist :
        pass

    return render_to_response('rango/category.html', context_dict, context)