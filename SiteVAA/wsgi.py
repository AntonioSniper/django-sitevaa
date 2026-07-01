import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SiteVAA.settings")

application = get_wsgi_application()

try:
    from django.conf import settings
    from django.contrib.auth import get_user_model

    User = get_user_model()

    if not User.objects.filter(username=settings.ADMIN_USERNAME).exists():
        User.objects.create_superuser(
            username=settings.ADMIN_USERNAME,
            email=settings.ADMIN_EMAIL,
            password=settings.ADMIN_PASSWORD,
        )
except Exception:
    pass