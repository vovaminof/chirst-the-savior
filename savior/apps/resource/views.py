from django.template.response import TemplateResponse
from savior.apps.resource.models import Resource, Category


def get_all_resources(req):
    context = {
        'resources': []
    }
    for category in Category.objects.all().order_by('order'):
        resources = Resource.objects.filter(category=category, active=True)
        if not resources:
            continue

        context['resources'].append({
            'items': resources,
            'category': category
        })

    without_category = Resource.objects.filter(category=None, active=True)
    if without_category:
        context['resources'].append({
            'items': without_category,
            'category': None
        })

    return TemplateResponse(req, 'resources.html', context)
