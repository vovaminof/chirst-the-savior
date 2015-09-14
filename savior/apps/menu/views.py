from django.conf import settings
from django.template.response import TemplateResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from savior.apps.menu.models import About, Ministry, Project, Course
from savior.apps.savior.models import Carousel
from savior.apps.service.models import Bulletin


def get_index(req):
    context = {
        'carousel_images': [],
        'bulletin': None
    }

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


def get_about(req, slug):
    obj = get_object_or_404(About, slug=slug + '/')
    context = {
        'item': model_to_dict(obj),
        'current': 'about'
    }

    return TemplateResponse(req, 'about.html', context)

def get_ministry(req, slug):
    obj = get_object_or_404(Ministry, slug=slug + '/')
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'ministries'
    }

    return TemplateResponse(req, 'ministry.html', context)

def get_project(req, slug):
    obj = get_object_or_404(Project, slug=slug + '/')
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'projects'
    }

    return TemplateResponse(req, 'project.html', context)

def get_course(req, slug):
    obj = get_object_or_404(Course, slug=slug + '/')
    data =  model_to_dict(obj)
    data['image'] = settings.MEDIA_URL + str(data['image'])
    context = {
        'item': data,
        'current': 'courses'
    }

    return TemplateResponse(req, 'course.html', context)