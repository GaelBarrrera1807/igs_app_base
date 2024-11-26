# iGrowSoft - Base App (app / module) - igs_app_base

## Tareas de ajuste en aplicación principal

En `configs/settings.py`

```python
...
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_bootstrap5',
    ...
    'igs_app_base',
    ...
]
...
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / "templates"],
        ...
        'APP_DIRS': True,
        ...
    },
]
...
FILE_UPLOAD_MAX_MEMORY_SIZE = 8400000
DATA_UPLOAD_MAX_MEMORY_SIZE = 5250000
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2500
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'
DATA_MIGRATION_DIR = 'datamigration'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_URL = 'session_login'
...
```

En `configs/urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static
...
urlpatterns = [
    ...
    path('', include('igs_app_base.urls')),
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
...
```

## Modelos implementados e interfaces
