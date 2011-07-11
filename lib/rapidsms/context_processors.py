from django.conf import settings
import warnings
def logo(request):
    try:
        base_template = settings.BASE_TEMPLATE
    except AttributeError:
        base_template = "layout.html"

    try:
        base_template_split_2 = settings.BASE_TEMPLATE_SPLIT_2
    except AttributeError:
        base_template_split_2 = "layout-split-2.html"

    return {'base_template': base_template,
            'base_template_split_2': base_template_split_2 }
