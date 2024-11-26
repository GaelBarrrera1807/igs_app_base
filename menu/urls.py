from .vw import views

obj = 'menuopc'
app_label = 'igs_app_base'

urlpatterns = views.create_urls(app_label)
