from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer
from django.utils.timezone import utc
from django.utils import timezone
import datetime
from django.db.models import Q
import importlib


from .models import Note, UniversityUser, User, QuizTest, \
    QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, \
    AnswerByUser, QuizResults, QuestionToResult, UserToGroup, Group, \
    QuizToGroup, QuizToCourse, Course, GroupToCourse, QuizPassing, AnswerToPassing


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'created_at')


class UserRegSer(RegisterSerializer):
    type = serializers.CharField(source='UniversityUser.type')

    class Meta:
        model = UniversityUser
        fields = ('id', 'username', 'email', 'password', 'type')

    def save(self, request):
        user_type = request.data['type']
        user = super().save(request)
        uni_user = UniversityUser(user=user, type=user_type)
        uni_user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='universityuser.type')
    # groups = GroupOfUsersSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'type', 'group_set')

class QuizAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ('id', 'answer_text', 'is_correct')

    def save(self, **kwargs):
        answer = super().save(**kwargs)
        checker = importlib.import_module('quiz.checkers.pifagor_checker')
        # print(dir(checker))
        answer.is_correct = checker.check(answer.answer_text)
        answer.save()
        # print(checker.check(answer.answer_text))
        return answer


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = QuizQuestion
        fields = ('id', 'quiz', 'text', 'answers', 'score', 'type')

class QuizTestSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True, read_only=True)
    readers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = QuizTest
        fields = ('id', 'title', 'author', 'questions', 'readers', 'max_time',
                  'max_attempts', 'groups_of_readers', 'courses', 'scoring_system', 'num_of_winners')

class QuizAnswerStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ('id', 'answer_text')


class QuizQuestionStudentSerializer(serializers.ModelSerializer):
    answers = QuizAnswerStudentSerializer(many=True, read_only=True)
    class Meta:
        model = QuizQuestion
        fields = ('id', 'quiz', 'text', 'answers', 'score', 'type')

class QuizTestStudentSerializer(serializers.ModelSerializer):
    questions = QuizQuestionStudentSerializer(many=True, read_only=True)
    readers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = QuizTest
        fields = ('id', 'title', 'author', 'questions', 'readers', 'max_time', 'max_attempts')

class AnswerToQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerToQuestion
        fields = ('answer', 'question')


class UserToQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToQuiz
        fields = ('quiz', 'user', 'id')

    def save(self, **kwargs):
        user = self.validated_data['user']
        quiz = self.validated_data['quiz']

        users_to_quiz = UserToQuiz.objects.filter(user_id=user.id, quiz_id=quiz.id)
        if users_to_quiz.count():
            user_to_quiz = users_to_quiz[0]
        else:
            user_to_quiz = super().save(**kwargs)

        return user_to_quiz


class AnswerByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerByUser
        fields = ('answer', 'user', 'id')


    def save(self, **kwargs):
        answer = self.validated_data['answer']
        user = self.validated_data['user']

        answers_by_user = AnswerByUser.objects.filter(answer_id=answer.id).filter(user_id=user.id)
        if answers_by_user.count():
            abu = answers_by_user[0]
        else:
            abu = super().save(**kwargs)


        question = abu.answer.questions.all()[0].question
        quiz = question.quiz
        quiz_results = QuizResults.objects.filter(quiz_id=quiz.id).filter(user_id=abu.user.id)

        answers_on_this_question_by_user = AnswerByUser.objects.filter(user_id=user.id). \
            filter(answer__questions__question_id=question.id)

        correct_answers_on_this_question_by_user = answers_on_this_question_by_user.filter(answer__is_correct=True)


        correct_answers_on_this_question = QuizQuestion.objects.filter(id=question.id). \
            filter(answers__is_correct=True)
        # print(question.type)
        if str(question.type) == '0':
            # print("+")
            count_of_correct_answers_on_this_question = correct_answers_on_this_question.count()
        else:
            count_of_correct_answers_on_this_question = 1
        # print("HERE", count_of_correct_answers_on_this_question)
        # for elem in correct_answers_on_this_question_by_user.all():
        #     print(elem)
        # print('Correct answers by user: ', correct_answers_on_this_question_by_user.count())

        if (quiz_results.count()):
            quiz_result = quiz_results[0]
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                    print("!!1")
                    if question not in quiz_result.correct_questions.all():
                        max_score_for_quiz = sum([question.score for question in quiz.questions.all()])

                        ans_to_res = QuestionToResult(question=question, result=quiz_result)
                        ans_to_res.save()
                        quiz_result.total_score += question.score
                        quiz_result.save()
                        quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                        quiz_result.save()
                else:
                    if question in quiz_result.correct_questions.all() :
                        max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                        QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                        quiz_result.total_score -= question.score
                        quiz_result.save()
                        quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                        quiz_result.save()
            else:
                if question in quiz_result.correct_questions.all():
                    max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                    QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                    quiz_result.total_score -= question.score
                    quiz_result.save()
                    quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                    quiz_result.save()
        else:
            score = 0
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                    score = question.score
                new_result = QuizResults(user=abu.user, quiz=quiz, total_score=score, percentage=score/max_score_for_quiz)
                new_result.save()
                if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                    ans_to_res = QuestionToResult(question=question, result=new_result)
                    ans_to_res.save()

        return abu

class QuestionToResultSerializer(serializers.ModelSerializer):
    question = QuizQuestionStudentSerializer(read_only=True)
    class Meta:
        model = QuestionToResult
        fields = ('question', 'result', 'show_in_res')

class QuizResultsSerializer(serializers.ModelSerializer):
    questions = QuestionToResultSerializer(many=True, read_only=True)

    class Meta:
        model = QuizResults
        fields = ('id',  'questions', 'total_score', 'percentage')

class UserToGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToGroup
        fields = ('user', 'group')

class GroupOfUsersSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('students', 'name', 'id')


class GroupToQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizToGroup
        fields = ('group', 'quiz', 'id')


    def save(self, **kwargs):
        group = self.validated_data['group']
        quiz = self.validated_data['quiz']
        group_to_quiz = QuizToGroup.objects.filter(group_id=group.id, quiz_id=quiz.id)
        if group_to_quiz.count():
            abu = group_to_quiz[0]
        else:
            abu = super().save(**kwargs)
        return abu


class CourseSerializer(serializers.ModelSerializer):
    groups = GroupOfUsersSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'groups', 'id')


class GroupToCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupToCourse
        fields = ('group', 'course')


class QuizToCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizToCourse
        fields = ('quiz', 'course', 'id')

    def save(self, **kwargs):
        quiz = self.validated_data['quiz']
        course = self.validated_data['course']
        quiz_to_course = QuizToCourse.objects.filter(quiz_id=quiz.id, course_id=course.id)

        if quiz_to_course.count():
            abu = quiz_to_course[0]
        else:
            abu = super().save(**kwargs)
        return abu

class AnswerToPassingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerToPassing
        fields = ('id', 'answer', 'passing')

    def save(self, **kwargs):
        answer = self.validated_data['answer']
        passing = self.validated_data['passing']

        answers_by_user = AnswerToPassing.objects.filter(answer_id=answer.id).filter(passing_id=passing.id)
        if answers_by_user.count():
            atp = answers_by_user[0]
        else:
            atp = super().save(**kwargs)
        user = atp.passing.user
        quiz = atp.passing.quiz
        results = atp.passing.result

        question = atp.answer.questions.all()[0].question
        # quiz = question.quiz
        quiz_results = QuizResults.objects.filter(id=results.id)

        answers_on_this_question_by_user = AnswerToPassing.objects.filter(passing_id=passing.id). \
            filter(answer__questions__question_id=question.id)

        correct_answers_on_this_question_by_user = answers_on_this_question_by_user.filter(answer__is_correct=True)

        correct_answers_on_this_question = QuizQuestion.objects.filter(id=question.id). \
            filter(answers__is_correct=True)
        print(question.type)
        if str(question.type) == '0':
            print("+")
            count_of_correct_answers_on_this_question = correct_answers_on_this_question.count()
        else:
            count_of_correct_answers_on_this_question = 1
        print("HERE", count_of_correct_answers_on_this_question)
        # for elem in correct_answers_on_this_question_by_user.all():
        #     print(elem)
        # print('Correct answers by user: ', correct_answers_on_this_question_by_user.count())

        correct_answers_on_this_question_by_other_users = \
            QuizResults.objects.filter(passing__quiz_id=quiz.id, correct_questions__id=question.id).filter(~Q(passing__user_id=user.id))
        l = [i for i in correct_answers_on_this_question_by_other_users.all()]
        s = set()
        for i in l:
            all = i.passing.all()
            for j in all:
                s.add(j.user_id)
                # print(dir(j))
        print('Kekekek', len(s))

        if (quiz_results.count()):

            quiz_result = quiz_results[0]
            print(quiz_result.id)
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                    print("!!1")
                    if question not in quiz_result.correct_questions.all():
                        max_score_for_quiz = sum([question.score for question in quiz.questions.all()])

                        show_in_res = False
                        if quiz.scoring_system == '1':
                            if (len(s) < quiz.num_of_winners):
                                quiz_result.total_score += question.score
                                quiz_result.save()
                                quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                                quiz_result.save()
                                show_in_res = True
                        else:
                            quiz_result.total_score += question.score
                            quiz_result.save()
                            quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                            quiz_result.save()
                            show_in_res = True
                        ans_to_res = QuestionToResult(question=question, result=quiz_result, show_in_res=show_in_res)
                        ans_to_res.save()
                else:
                    if question in quiz_result.correct_questions.all():
                        print("!!2")
                        max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                        QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                        quiz_result.total_score -= question.score
                        quiz_result.save()
                        quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                        quiz_result.save()
            else:
                if question in quiz_result.correct_questions.all():
                    print("!!3")
                    max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                    QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                    quiz_result.total_score -= question.score
                    quiz_result.save()
                    quiz_result.percentage = quiz_result.total_score / max_score_for_quiz
                    quiz_result.save()
        else:
            score = 0
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                max_score_for_quiz = sum([question.score for question in quiz.questions.all()])
                show_in_res = False
                if quiz.scoring_system == '1':
                    if len(s) < quiz.num_of_winners:
                        if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                            score = question.score
                            show_in_res = True
                else:
                    if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                        score = question.score
                        show_in_res = True
                new_result = QuizResults(total_score=score,
                                         percentage=score / max_score_for_quiz)
                new_result.save()
                atp.passing.result = new_result
                atp.save()
                if correct_answers_on_this_question_by_user.count() == count_of_correct_answers_on_this_question:
                    ans_to_res = QuestionToResult(question=question, result=new_result, show_in_res=show_in_res)
                    ans_to_res.save()

        return atp

class QuizPassingSerializer(serializers.ModelSerializer):
    result = QuizResultsSerializer(read_only=True)
    answers = QuizAnswerSerializer(many=True, read_only=True)
    remaining_time = serializers.ReadOnlyField()
    remaining_attempts = serializers.ReadOnlyField()
    seconds_per_end = serializers.ReadOnlyField()
    is_going = serializers.ReadOnlyField()

    class Meta:
        model = QuizPassing
        fields = ('id', 'quiz', 'user', 'result', 'answers', 'start_time', 'duration', 'end_time',
                  'remaining_time', 'attempt', 'remaining_attempts', 'seconds_per_end', 'is_going')

    def save(self, **kwargs):
        quiz = self.validated_data['quiz']
        user = self.validated_data['user']
        query = QuizPassing.objects.filter(quiz_id=quiz.id, user_id=user.id).order_by('start_time')

        last = query.all().last()
        if last:
            now = timezone.now()
            # print(now)
            # print(timezone.now())
            # print(last.start_time)
            timediff = now - last.start_time
            timediff_in_minutes = timediff.total_seconds() / 60

            timediff2 = now - last.end_time
            # print(last.attempt)
            # print(last.quiz.max_attempts)
            if (timediff_in_minutes > last.duration or timediff2.total_seconds() > 0) and last.attempt < last.quiz.max_attempts:
                result = QuizResults()
                result.save()
                print('Kek')
                now = timezone.now()
                duration = quiz.max_time
                new_passing = super().save(quiz=quiz, user=user, start_time=now, duration=duration, result=result,
                                           end_time=now + datetime.timedelta(minutes=duration + 1), attempt=last.attempt + 1)
                return new_passing
            else:
                print('Hui')
                print(last)
                return last
        else:
            print('Ebat')
            result = QuizResults()
            result.save()
            now = timezone.now()
            duration = quiz.max_time
            new_passing = super().save(quiz=quiz, user=user, start_time=datetime.datetime.utcnow(), duration=duration, result=result,
                                       end_time=now + datetime.timedelta(minutes=duration + 1), attempt=1)
            return new_passing



def jwt_token_payload_handler(token, user, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


