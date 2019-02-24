# -*- coding: utf-8 -*-

from savior.apps.savior.models import Footer


def footer_processor(response):
    try:
        obj = Footer.objects.get()
    except Footer.DoesNotExist:
        return {'footer': {}}

    return {'footer': obj}

