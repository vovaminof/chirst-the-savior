from django.conf import settings

from django.forms.models import model_to_dict
from django.template.response import TemplateResponse

from savior.apps.savior.models import Carousel

def index(req):
    context = {
        'carousel_images': []
    }

    for obj in Carousel.objects.get_active():
        data = model_to_dict(obj)
        data['image'] = settings.MEDIA_URL + str(data['image'])
        context['carousel_images'].append(data)

    return TemplateResponse(req, 'index.html', context)