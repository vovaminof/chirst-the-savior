import re
import time
from datetime import datetime, timedelta

from taggit.models import Tag

from django.conf import settings
from django.http import Http404
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from savior.apps.event.models import Event

default_fields = ['id', 'title', 'title_color', 'description', 'recurrences', 'place',
                  'recurrences__occurrence__datetime', 'recurrences__duration', 
                  'recurrences__occurrence__id']

def format_event(data):
    result = []

    if 'image' in data:
        data['image'] = settings.MEDIA_URL + str(data['image'])
    
    data['date_start'] = data.pop('recurrences__occurrence__datetime')
    duration = data.pop('recurrences__duration')
    duration = timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
    if duration != timedelta(0):
        data['date_end'] = data['date_start'] + duration

    data['occurrence_id'] = data.pop('recurrences__occurrence__id')

    return data

def get_event(req, event_id, occurrence_id):
    events = Event.objects.select_related('recurrences', 'recurrences__occurrence')
    try:
        obj = Event.objects.filter(pk=event_id, recurrences__occurrence__id=occurrence_id) \
                           .values(*(default_fields + ['image']))[0]
        tags = Event.objects.get(id=obj['id']).tags.all()
    except IndexError:
        raise Http404

    context = {
        'event': format_event(obj),
        'tags': [tag.name for tag in tags]
    }

    return TemplateResponse(req, 'event-single.html', context)

def get_all_events(req):
    tag = req.GET.get('tag', '')
    events_list = Event.objects.filter(recurrences__occurrence__datetime__gt=datetime.now())

    if tag:
        events_list = events_list.filter(tags__name__in=[tag])

    events_list = events_list.order_by('recurrences__occurrence__datetime') \
                             .values(*default_fields)
    paginator = Paginator(events_list, 5)

    page = req.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    start_page = max(1, min(events.number - 2, events.paginator.num_pages - 4))
    end_page = min(max(events.number + 2, 5), events.paginator.num_pages)
    pages = range(start_page, end_page + 1)

    context = {
        'events': [format_event(event) for event in events],
        'handler': events,
        'pages': pages,
        'current_tag': tag,
        'tags': [tag.name for tag in Tag.objects.all()],
        'current': 'events'
    }

    return TemplateResponse(req, 'events.html', context)