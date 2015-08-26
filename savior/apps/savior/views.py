from django.shortcuts import redirect
from django.forms.models import model_to_dict

from savior.apps.savior.models import PrayerRequest
from savior.lib.utils.views import JSONResponse


def send_request(req):
    if req.method == 'POST':
        name = req.POST.get('name', '').strip()
        if not name:
            return JSONResponse({
                'error': {
                    'msg': 'Name filed is required.', 
                    'field': 'name'
                }
            })

        if len(name) > 64:
            return JSONResponse({
                'error': {
                    'msg': 'Max length of name field is 64 characters.', 
                    'field': 'name'
                }
            })

        text = req.POST.get('text', '').strip()
        if not text:
            return JSONResponse({
                'error': {
                    'msg': 'Text filed is required.', 
                    'field': 'text'
                }
            })

        if len(text) > 500:
            return JSONResponse({
                'error': {
                    'msg': 'Max length of text field 500 characters.', 
                    'field': 'text'
                }
            })

        PrayerRequest.objects.create(name=name, text=text)

        return JSONResponse({'success': 'ok'})

    return redirect('savior-index')