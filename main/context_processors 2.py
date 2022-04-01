from django.utils.translation import get_language


def get_language_info(request):
    context = {
        'lang': get_language(),
    }
    return context
