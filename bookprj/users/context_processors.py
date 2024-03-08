from django.conf import settings

def avatarProcessor(request):
    if request.user.is_authenticated:
        user = request.user
        profile = user.profile
        if profile.avatar_path:
            avatar_path = settings.MEDIA_URL + profile.avatar_path
        else:
            avatar_path = None
        return {'avatar_path': avatar_path, 'currentUser':user}
    return {'avatar_path': None, "currentUser":None}