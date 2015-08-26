from savior.apps.menu.models import About, Ministry, Project, Course

def menu_processor(response):
    data = {
        'about': [],
        'ministries': [],
        'projects': [],
        'courses': []
    }

    for obj in About.objects.get_active().values('slug', 'title'):
        data['about'].append(obj)

    for obj in Ministry.objects.get_active().values('slug', 'title'):
        data['ministries'].append(obj)

    for obj in Project.objects.get_active().values('slug', 'title'):
        data['projects'].append(obj)

    for obj in Course.objects.get_active().values('slug', 'title'):
        data['courses'].append(obj)

    return {'menu': data}