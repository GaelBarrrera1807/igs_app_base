from .vw import views

obj = 'permission'
app_label = 'auth'

urlpatterns = views.create_urls(app_label)
