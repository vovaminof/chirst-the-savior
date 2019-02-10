from django.template.response import TemplateResponse
from savior.apps.resource.models import Resource, Category, File, Book


def get_all_resources(req):
    context = {
        'resources': [],
        'current': 'resources'
    }
    for category in Category.objects.all().order_by('order'):
        resources = Resource.objects.filter(category=category, active=True).order_by('order')

        items = []
        for resource in resources:
            items.append({
                "title": resource.title,
                "type": "resource",
                "formats": resource.file_set.all()
            })

        books = Book.objects.filter(category=category, active=True).order_by('order')
        for book in books:
            items.append({
                "title": book.title,
                "type": "book",
                "pk": book.pk
            })

        if items:
            context['resources'].append({
                'items': items,
                'category': category
            })

    return TemplateResponse(req, 'resources.html', context)


def get_book(req, book_id):
    book = Book.objects.get(pk=book_id)
    return TemplateResponse(req, 'book.html', {"book": book})

