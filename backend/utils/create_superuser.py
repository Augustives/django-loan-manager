import os

from django.contrib.auth.models import User
from django.db import IntegrityError

try:
    superuser = User.objects.create_superuser(
        username=os.environ.get("SUPER_USER_NAME", default="admin"),
        email=os.environ.get("SUPER_USER_EMAIL", default="admin@gmail.com"),
        password=os.environ.get("SUPER_USER_PASSWORD", default="admin"),
    )
    superuser.save()
except IntegrityError:
    print(f"Failed to automatically create super user!")
