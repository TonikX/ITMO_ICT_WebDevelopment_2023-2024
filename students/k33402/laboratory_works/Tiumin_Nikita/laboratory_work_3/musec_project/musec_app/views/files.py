from rest_framework.decorators import api_view
from musec_app.models import File
from musec_app.responses import api_response
import os
from django.http import HttpResponse
from django.conf import settings


@api_view(['GET'])
def download_audio(_, filename):
    return get_response('audio/mpeg', filename)


@api_view(['GET'])
def download_image(_, filename):
    return get_response('image/png', filename)


def get_response(content_type, filename):
    filename = 'storage/' + filename
    file = File.objects.filter(file=filename).all().first()
    if not file:
        return api_response.not_found()

    full_path = os.path.join(settings.MEDIA_ROOT, filename)

    with open(full_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type=content_type)
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(full_path)
        return response
