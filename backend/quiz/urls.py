from rest_framework import routers
from django.conf.urls import url

from .views import NoteViewSet, UserViewSet, QuizTestViewSet, QuizAnswerViewSet, \
    QuizQuestionViewSet, QuizTestDetails, UserDetails, QuizQuestionDetails, AnswerToQauestionVS, \
    UserToQuizVS, StudentsViewSet, AnswerByUserViewSet, UserQuizResultsViewSet, \
    UserToGroupViewSet, GroupViewSet, GroupToQuizViewSet, CourseViewSet, QuizToCourseViewSet, \
    QuizPassingViewSet, QuizPassingDetails, AnswerToPassingViewSet, QuizPassingLastViewSet, \
    QuizPassingStop, CheckerView, MyCheckerView, UserSetAvatar


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tests', QuizTestViewSet)
router.register(r'answers', QuizAnswerViewSet)
router.register(r'questions', QuizQuestionViewSet)
router.register(r'answer_to_question', AnswerToQauestionVS)
router.register(r'user_to_quiz', UserToQuizVS)
router.register(r'students', StudentsViewSet)
router.register(r'results', UserQuizResultsViewSet)
router.register(r'user_to_group', UserToGroupViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'quiz_to_group', GroupToQuizViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'quiz_to_course', QuizToCourseViewSet)
router.register(r'passing', QuizPassingViewSet)
router.register(r'answer_to_passing', AnswerToPassingViewSet)
router.register(r'checker', CheckerView)
router.register(r'my_checker', MyCheckerView)
router.register(r'set_avatar', UserSetAvatar)

urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetails.as_view()),
    url(r'^test/(?P<pk>[0-9]+)/$', QuizTestDetails.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', QuizQuestionDetails.as_view()),
    url(r'^passing_details/(?P<pk>[0-9]+)/$', QuizPassingDetails.as_view()),
    url(r'^stop_passing/(?P<pk>[0-9]+)/$', QuizPassingStop.as_view()),
    url(r'^last_passing/(?P<pk>[0-9]+)/$', QuizPassingLastViewSet.as_view()),
]

urlpatterns += router.urls


