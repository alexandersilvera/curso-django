from django.http import HttpResponse


def home(request):
    raise ValueError()
    return HttpResponse('<html><body>Hola Mundo</body></html>', content_type='text/html')
