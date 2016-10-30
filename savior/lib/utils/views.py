import json

from django.conf import settings
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        output = json.dumps(data)
        super(JSONResponse, self).__init__(output, mimetype='application/json',
                                           **kwargs)


def get_image_url(image):
    if image:
        image = settings.MEDIA_URL + str(image)

    return image
