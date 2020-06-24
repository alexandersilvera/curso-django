from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Hola Mundo</body></html>', content_type='text/html')
