from django.db.models import QuerySet
from django.db.models import Q
from rest_framework import viewsets, generics

from .models import Note, User, QuizTest, QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, AnswerByUser, \
    QuizResults, QuestionToResult, UserToGroup, Group, QuizToGroup, Course, GroupToCourse, QuizToCourse

from .enums import UniUser
from .serializers import NoteSerializer, UserSerializer, QuizTestSerializer,\
    QuizQuestionSerializer, QuizAnswerSerializer, AnswerToQuestionSerializer, \
    UserToQuizSerializer, QuizQuestionStudentSerializer, QuizTestStudentSerializer, \
    AnswerByUserSerializer, QuizResultsSerializer, UserToGroupSerializer, GroupOfUsersSerializer, \
    GroupToQuizSerializer, CourseSerializer, GroupToCourseSerializer, QuizToCourseSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('universityuser')
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all().select_related('universityuser')
    serializer_class = UserSerializer

class QuizTestViewSet(viewsets.ModelViewSet):
    queryset = QuizTest.objects.all()
    serializer_class = QuizTestSerializer

    def get_serializer_class(self):
        try:
            if self.request.user.universityuser.type == UniUser.TEACHER.value:
                return QuizTestSerializer
            elif self.request.user.universityuser.type == UniUser.STUDENT.value:
                return QuizTestStudentSerializer
        except Exception as e:
            return QuizTestSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            if self.request.user.universityuser.type == UniUser.TEACHER.value:
                return queryset.filter(author_id=self.request.user.id)
            elif self.request.user.universityuser.type == UniUser.STUDENT.value:
                # print(dir(self.request.user))
                # print(self.request.user.group_set.all())
                curr_groups = [elem.id for elem in self.request.user.group_set.all()]
                curr_courses = []
                for elem in self.request.user.group_set.all():
                    for course in elem.course_set.all():
                        curr_courses.append(course.id)
                # print(dir(curr_groups))
                return queryset.filter(Q(courses__in=curr_courses) | Q(groups_of_readers__in=curr_groups) | Q(readers__id=self.request.user.id))
                # return queryset.filter(readers__id=self.request.user.id)
        except Exception as e:
            return  queryset

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('universityuser').filter(universityuser__type=UniUser.STUDENT.value)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return queryset

class QuizTestDetails(generics.RetrieveAPIView):
    queryset = QuizTest.objects.all()

    def get_serializer_class(self):
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return QuizTestSerializer
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return QuizTestStudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return queryset.filter(author_id=self.request.user.id)
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            curr_groups = [elem.id for elem in self.request.user.group_set.all()]
            curr_courses = []
            for elem in self.request.user.group_set.all():
                for course in elem.course_set.all():
                    curr_courses.append(course.id)
            # print(dir(curr_groups))
            return queryset.filter(Q(courses__in=curr_courses) | Q(groups_of_readers__in=curr_groups) | Q(
                readers__id=self.request.user.id))

class QuizAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

    # def get_serializer_class(self):
    #     if self.request.user.universityuser.type == UniUser.TEACHER.value:
    #         return QuizQuestionSerializer
    #     elif self.request.user.universityuser.type == UniUser.STUDENT.value:
    #         return QuizQuestionStudentSerializer

class QuizQuestionDetails(generics.RetrieveAPIView):
    queryset = QuizQuestion.objects.all()

    def get_serializer_class(self):
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return QuizQuestionSerializer
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return QuizQuestionStudentSerializer

class AnswerToQauestionVS(viewsets.ModelViewSet):
    queryset = AnswerToQuestion.objects.all()
    serializer_class = AnswerToQuestionSerializer

class UserToQuizVS(viewsets.ModelViewSet):
    queryset = UserToQuiz.objects.all()
    serializer_class = UserToQuizSerializer


class AnswerByUserViewSet(viewsets.ModelViewSet):
    queryset = AnswerByUser.objects.all()
    serializer_class = AnswerByUserSerializer

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        answer = resp.data['answer']
        user = resp.data['user']
        abu = AnswerByUser.objects.filter(answer_id=answer, user_id=user)[0]
        resp.data['id'] = abu.id
        resp.data['question'] = abu.answer.questions.filter(answer_id=answer)[0].question.id
        return resp

    def destroy(self, request, *args, **kwargs):
        id = kwargs['pk']
        abu = AnswerByUser.objects.get(id=id)
        question = abu.answer.questions.filter(answer_id=abu.answer)[0].question
        quiz = question.quiz
        user = abu.user
        results = QuizResults.objects.filter(user_id=user.id, quiz_id=quiz.id)

        if abu.answer.is_correct:
            if results.count():
                result = results[0]
                if question in result.correct_questions.all():
                    max_score_for_quiz = sum([q.score for q in quiz.questions.all()])
                    QuestionToResult.objects.filter(question_id=question.id, result_id=result.id).delete()
                    result.total_score -= question.score
                    result.save()
                    result.percentage = result.total_score / max_score_for_quiz
                    result.save()
        else:
            print('SUBMIIIIIIT TIME')
        return super().destroy(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.universityuser.type == UniUser.TEACHER.value:
    #         return queryset.filter(answer__question__quiz__author_id=self.request.user.id)
    #     elif self.request.user.universityuser.type == UniUser.STUDENT.value:
    #         return queryset.filter(user_id=self.request.user.id)


class UserQuizResultsViewSet(viewsets.ModelViewSet):
    queryset = QuizResults.objects.all()
    serializer_class = QuizResultsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            if self.request.user.universityuser.type == UniUser.TEACHER.value:
                return queryset.filter(quiz_author_id=self.request.user.id)
            elif self.request.user.universityuser.type == UniUser.STUDENT.value:
                return queryset.filter(user_id=self.request.user.id)
        except Exception as e:
            return queryset

    def destroy(self, request, *args, **kwargs):
        id = kwargs['pk']
        res = QuizResults.objects.get(id=id)
        user = res.user
        quiz = res.quiz
        for question in quiz.questions.all():
            AnswerByUser.objects.filter(user_id=user.id, answer__questions__question_id=question.id).delete()
        return super().destroy(request, *args, **kwargs)


class UserToGroupViewSet(viewsets.ModelViewSet):
    queryset = UserToGroup.objects.all()
    serializer_class = UserToGroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupOfUsersSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            if self.request.user.universityuser.type == UniUser.STUDENT.value:
                return queryset.filter(students_id=self.request.user.id)
            else:
                return queryset
        except Exception as e:
            return queryset


class GroupToQuizViewSet(viewsets.ModelViewSet):
    queryset = QuizToGroup.objects.all()
    serializer_class = GroupToQuizSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.STUDENT.value:
            return queryset.filter(group_students_id=self.request.user.id)
        else:
            return queryset


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            if self.request.user.universityuser.type == UniUser.STUDENT.value:
                return queryset.filter(groups__students_id=self.request.user.id)
            else:
                return queryset
        except Exception as e:
            return queryset

class QuizToCourseViewSet(viewsets.ModelViewSet):
    queryset = QuizToCourse.objects.all()
    serializer_class = QuizToCourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            if self.request.user.universityuser.type == UniUser.STUDENT.value:
                return queryset.filter(course_groups__students_id=self.request.user.id)
            else:
                return queryset
        except Exception as e:
            return queryset
