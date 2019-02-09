from django.template.response import TemplateResponse
from savior.apps.resource.models import Resource, Category, File


def get_all_resources(req):
    context = {
        'resources': [],
        'current': 'resources'
    }
    for category in Category.objects.all().order_by('order'):
        resources = Resource.objects.filter(category=category, active=True).order_by('order')
        if not resources:
            continue

        items = []
        for resource in resources:
            items.append({
                "title": resource.title,
                "formats": resource.file_set.all()
            })
        context['resources'].append({
            'items': items,
            'category': category
        })

    without_category = Resource.objects.filter(category=None, active=True)
    if without_category:
        context['resources'].append({
            'items': without_category,
            'category': None
        })

    return TemplateResponse(req, 'resources.html', context)
