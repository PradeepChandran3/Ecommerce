from.models import Category
def Menu_Links(request):
    links=Category.objects.all()
    return dict(links=links)
