from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^api/v1/', include('quiz.urls')),
    url(r'^api/v1/rest-auth-jwt/', obtain_jwt_token),
    url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/refresh-token/', refresh_jwt_token),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.CHECKER_URL, document_root=settings.CHECKER_ROOT)