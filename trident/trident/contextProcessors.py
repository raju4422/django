
def common(request):
    context = {
        'userdata': request.user
    }
    return context
