from One_project.settings import VERSION

def version(request):
    return {'version':VERSION}
