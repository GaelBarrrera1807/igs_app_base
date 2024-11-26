from .vw import views

obj = 'group'
app_label = 'auth'

urlpatterns = views.create_urls(app_label)
