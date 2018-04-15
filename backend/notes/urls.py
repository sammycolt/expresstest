from rest_framework import routers
from django.conf.urls import url

from .views import NoteViewSet, UserViewSet, QuizTestViewSet, QuizAnswerViewSet, \
    QuizQuestionViewSet, QuizTestDetails, UserDetails, QuizQuestionDetails, AnswerToQauestionVS

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)
router.register(r'tests', QuizTestViewSet)
router.register(r'answers', QuizAnswerViewSet)
router.register(r'questions', QuizQuestionViewSet)
router.register(r'answer_to_question', AnswerToQauestionVS)

urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetails.as_view()),
    url(r'^test/(?P<pk>[0-9]+)/$', QuizTestDetails.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', QuizQuestionDetails.as_view()),
]

urlpatterns += router.urls
