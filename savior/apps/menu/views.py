from geopy.geocoders import GoogleV3

from django.db.models import Q
from django.conf import settings
from django.template.response import TemplateResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from savior.apps.menu.models import About, Ministry, Project, Course, Contact
from savior.apps.savior.models import Carousel
from savior.apps.service.models import Bulletin
from savior.apps.blog.models import Post
from savior.apps.blog.views import format_post

geolocator = GoogleV3()


def get_index(req):
    context = {
        'carousel_images': [],
        'bulletin': None,
        'latest_posts': []
    }

    for post in Post.objects.filter(published=True).order_by('-ctime')[:settings.INDEX_POSTS_LIMIT]:
        context['latest_posts'].append(format_post(post))

    for obj in Carousel.objects.get_active():
        data = model_to_dict(obj)
        data['image'] = settings.MEDIA_URL + str(data['image'])
        context['carousel_images'].append(data)

    try:
        bulletin = Bulletin.objects.order_by('-publish_date')[0]
        data = model_to_dict(bulletin)
        context['bulletin'] = {
            'src': settings.MEDIA_URL + str(data['src']),
            'publish_date': '{:%d-%m-%Y}'.format(data['publish_date'])
        }
    except IndexError:
        pass

    return TemplateResponse(req, 'index.html', context)


def get_contact(req):
    obj = get_object_or_404(Contact)
    data = model_to_dict(obj)
    location = geolocator.reverse('{0},{1}'.format(data['address'].latitude, data['address'].longitude), timeout=5)
    data['readable_address'] = location[0].address.replace('Poland', 'Polska')

    context = {
        'item': data,
        'current': 'contact',
        'maps_api': settings.MAPS_API
    }
    return TemplateResponse(req, 'contact.html', context)


def get_about(req, slug):
    obj = get_object_or_404(About, Q(slug_pl=slug + '/') | Q(slug_en=slug + '/'))
    context = {
        'item': model_to_dict(obj),
        'current': 'about'
    }

    return TemplateResponse(req, 'about.html', context)

def get_ministry(req, slug):
    obj = get_object_or_404(Ministry, Q(slug_pl=slug + '/') | Q(slug_en=slug + '/'))
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'ministries'
    }

    return TemplateResponse(req, 'ministry.html', context)

def get_project(req, slug):
    obj = get_object_or_404(Project, Q(slug_pl=slug + '/') | Q(slug_en=slug + '/'))
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'projects'
    }

    return TemplateResponse(req, 'project.html', context)

def get_course(req, slug):
    obj = get_object_or_404(Course, Q(slug_pl=slug + '/') | Q(slug_en=slug + '/'))
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'courses'
    }

    return TemplateResponse(req, 'course.html', context)