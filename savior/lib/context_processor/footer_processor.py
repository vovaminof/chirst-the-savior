from geopy.geocoders import GoogleV3

from django.forms.models import model_to_dict

from savior.apps.savior.models import Footer

geolocator = GoogleV3()


def footer_processor(response):
    try:
        obj = Footer.objects.get()
    except Footer.DoesNotExist:
        return {'footer': {}}

    data = model_to_dict(obj)

    location = geolocator.reverse('{0},{1}'.format(obj.contact.address.latitude, obj.contact.address.longitude),
                                  timeout=5)

    data['readable_address'] = location[0].address.replace('Poland', 'Polska')
    data['phone'] = obj.contact.phone
    data['email'] = obj.contact.email

    del data['contact']

    return {'footer': data}