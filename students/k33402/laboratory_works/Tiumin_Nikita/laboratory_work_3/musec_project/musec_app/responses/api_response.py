from django.http import JsonResponse


def success(message='Success'):
    return JsonResponse(
        data=format_payload(message),
        status=200
    )


def payload(data):
    return JsonResponse(
        data=format_payload(data=data),
        status=200
    )


#  Errors
def unauthenticated():
    return JsonResponse(
        data=format_payload('Invalid credentials'),
        status=401
    )


def validation_error(errors, message='Validation error'):
    return JsonResponse(
        data=format_payload(message, None, errors),
        status=422
    )


def not_found(message='Not found'):
    return JsonResponse(
        data=format_payload(message),
        status=404,
    )


def error(message='Error', status=400):
    return JsonResponse(
        data=format_payload(message),
        status=status
    )


#  Internal
def format_payload(message=None, data=None, errors=None):
    return {
        'message': message,
        'data': data if data else [],
        'errors': errors if errors else [],
    }
