import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import { User } from '../api/users'
import { Test } from '../api/tests'
import { Answer } from '../api/answers'
import { Question } from '../api/questions'
import { Group } from '../api/groups'
import { Course } from '../api/courses'
import { Passing } from '../api/passing'
import {
  ADD_NOTE,
  REMOVE_NOTE,
  SET_NOTES,
  ADD_USER,
  SET_USERS,
  LOGIN_USER,
  LOGOUT_USER,
  ADD_TEST,
  ADD_ANSWER,
  ADD_QUESTION,
  SET_TESTS,
  SET_ANSWERS,
  SET_QUESTIONS,
  SET_USER_DETAILS,
  ADD_USER_DETAILS,
  ADD_TEST_DETAILS,
  ADD_QUESTION_DETAILS,
  SET_STUDENTS,
  ADD_ANSWER_BY_USER,
  SET_ANSWERS_BY_USER,
  SET_GIVEN_ANSWERS,
  SET_STUDENTS_DICTIONARY,
  ADD_ID_TO_GIVEN_ANSWERS,
  REMOVE_ANSWER_BY_USER,
  SET_TEST_RESULTS,
  REMOVE_TEST_RESULT,
  SET_GROUPS,
  SET_GROUPS_DICTIONARY,
  SET_COURSES,
  SET_COURSES_DICTIONARY,
  REMOVE_TEST,
  REMOVE_QUESTION,
  REMOVE_ANSWER,
  SET_PASSING,
  SET_PASSING_TO_TEST,
  SET_COURSE_TO_TEST
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  notes: [],
  users: [],
  tests: [],
  answers: [],
  questions: [],
  isLogged: !!localStorage.getItem('token'),
  userInfo: localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo')) : {},
  userDetails: {},
  testDetails: {},
  questionDetails: {},
  students: [],
  answersByUser: [],
  givenAnswers: {},
  studentsDictionaryByUsername: {},
  studentsDictionaryById: {},
  testResults: {},
  groups: [],
  groupsDictionaryByName: {},
  groupsDictionaryById: {},
  courses: [],
  coursesDictionaryByName: {},
  coursesDictionaryById: {},
  passing: {},
  courseToTests: {}
}

const getters = {
  notes: state => state.notes,
  users: state => state.users,
  tests: state => state.tests,
  answers: state => state.answers,
  questions: state => state.questions,
  isLogged: state => state.isLogged,
  userInfo: state => state.userInfo,
  userDetails: state => state.userDetails,
  testDetails: state => state.testDetails,
  questionDetails: state => state.questionDetails,
  students: state => state.students,
  givenAnswers: state => state.givenAnswers,
  testResults: state => state.testResults,
  studentsDictionaryByUsername: state => state.studentsDictionaryByUsername,
  groups: state => state.groups,
  groupsDictionaryByName: state => state.groupsDictionaryByName,
  courses: state => state.courses,
  coursesDictionaryByName: state => state.coursesDictionaryByName
}

const mutations = {
  [ADD_NOTE] (state, note) {
    state.notes = [note, ...state.notes]
  },
  [REMOVE_NOTE] (state, { id }) {
    state.notes = state.notes.filter(note => {
      return note.id !== id
    })
  },
  [SET_NOTES] (state, { notes }) {
    state.notes = notes
  },
  [ADD_USER] (state, user) {
    state.users = [user, ...state.users]
  },
  [SET_USERS] (state, { users }) {
    state.users = users
  },
  [LOGIN_USER] (state, userInfo) {
    state.isLogged = true
    state.userInfo = userInfo
  },

  [LOGOUT_USER] (state) {
    state.isLogged = false
    state.userInfo = {}
  },
  [ADD_TEST] (state, test) {
    state.tests = [test, ...state.tests]
  },
  [SET_TESTS] (state, { tests }) {
    state.tests = tests
  },
  [ADD_QUESTION] (state, question) {
    state.questions = [question, ...state.questions]
  },
  [SET_QUESTIONS] (state, { questions }) {
    state.questions = questions
  },
  [ADD_ANSWER] (state, answer) {
    state.answers = [answer, ...state.answers]
  },
  [SET_ANSWERS] (state, { answers }) {
    state.answers = answers
  },
  [SET_USER_DETAILS] (state, userDetails) {
    state.userDetails = userDetails
  },
  [ADD_USER_DETAILS] (state, payload) {
    Vue.set(state.userDetails, payload.key, payload.value)
  },
  [ADD_TEST_DETAILS] (state, payload) {
    Vue.set(state.testDetails, payload.key, payload.value)
  },
  [ADD_QUESTION_DETAILS] (state, payload) {
    Vue.set(state.questionDetails, payload.key, payload.value)
  },
  [SET_STUDENTS] (state, { students }) {
    state.students = students
  },
  [ADD_ANSWER_BY_USER] (state, answerByUser) {
    state.answersByUser = [answerByUser, ...state.answersByUser]
  },
  [SET_ANSWERS_BY_USER] (state, { answers }) {
    state.answersByUser = answers
  },
  [REMOVE_ANSWER_BY_USER] (state, { id }) {
    state.answersByUser = state.answersByUser.filter(abu => {
      return abu.id !== id
    })
  },
  [SET_GIVEN_ANSWERS] (state, testId) {
    if (!state.givenAnswers.length) {
      var ans = {}
      var questions = state.testDetails[testId].questions
      for (var i = 0; i < questions.length; ++i) {
        Vue.set(ans, questions[i].id, {'given': false})
        for (var j = 0; j < questions[i].answers.length; ++j) {
          Vue.set(ans[questions[i].id], questions[i].answers[j].id, {'given': false})
        }
      }
      Vue.set(state, 'givenAnswers', ans)
    }
  },
  [ADD_ID_TO_GIVEN_ANSWERS] (state, payload) {
    // console.log(payload)
    if (state.givenAnswers) {
      var question = payload.question
      var answer = payload.answer
      var abuId = payload.id
      Vue.set(state.givenAnswers[question][answer], 'answerByUserId', abuId)
    }
  },
  [SET_STUDENTS_DICTIONARY] (state) {
    if (!state.studentsDictionaryByUsername.length) {
      var students = {}
      for (var i = 0; i < state.students.length; ++i) {
        students[state.students[i].username] = state.students[i]
      }
      Vue.set(state, 'studentsDictionaryByUsername', students)
    }
    if (!state.studentsDictionaryById.length) {
      var students1 = {}
      for (var j = 0; j < state.students.length; ++j) {
        students1[state.students[j].id] = state.students[j]
      }
      Vue.set(state, 'studentsDictionaryById', students1)
    }
  },
  [SET_TEST_RESULTS] (state, passings) {
    var res = {}
    for (var i = 0; i < passings.length; ++i) {
      var result = passings[i].result
      result['quiz'] = passings[i].quiz
      result['user'] = passings[i].user
      result['remaining_time'] = passings[i].remaining_time
      // result['time'] = passings[i].
      if (!res[passings[i].quiz]) {
        res[passings[i].quiz] = [result]
      } else {
        res[passings[i].quiz] = [result, ...res[passings[i].quiz]]
      }
    }
    state.testResults = res
  },
  [REMOVE_TEST_RESULT] (state, { testId }) {
    Vue.set(state.testResults, testId, {})
  },
  [SET_GROUPS] (state, { groups }) {
    state.groups = groups
  },
  [SET_GROUPS_DICTIONARY] (state) {
    if (!state.groupsDictionaryByName.length) {
      var groups = {}
      for (var i = 0; i < state.groups.length; ++i) {
        groups[state.groups[i].name] = state.groups[i]
      }
      Vue.set(state, 'groupsDictionaryByName', groups)
    }
    if (!state.groupsDictionaryById.length) {
      var groups1 = {}
      for (var j = 0; j < state.groups.length; ++j) {
        groups1[state.groups[j].id] = state.groups[j]
      }
      Vue.set(state, 'groupsDictionaryById', groups1)
    }
  },
  [SET_COURSES] (state, { courses }) {
    state.courses = courses
  },
  [SET_COURSES_DICTIONARY] (state) {
    if (!state.coursesDictionaryByName.length) {
      var courses = {}
      for (var i = 0; i < state.courses.length; ++i) {
        courses[state.courses[i].name] = state.courses[i]
      }
      Vue.set(state, 'coursesDictionaryByName', courses)
    }
    if (!state.coursesDictionaryById.length) {
      var courses1 = {}
      for (var j = 0; j < state.courses.length; ++j) {
        courses1[state.courses[j].id] = state.courses[j]
      }
      Vue.set(state, 'coursesDictionaryById', courses1)
    }
  },
  [REMOVE_TEST] (state, id) {
    Vue.set(state, 'tests', state.tests.filter(test => {
      return test.id !== id
    }))
  },
  [REMOVE_QUESTION] (state, payload) {
    var questionId = payload.questionId
    var testId = payload.testId
    Vue.set(state, 'questions', state.questions.filter(question => {
      return question.id !== questionId
    }))
    Vue.set(state.testDetails[testId], 'questions', state.testDetails[testId].questions.filter(question => {
      return question.id !== questionId
    }))
  },
  [REMOVE_ANSWER] (state, payload) {
    var questionId = payload.questionId
    var answerId = payload.answerId
    Vue.set(state, 'answers', state.answers.filter(answer => {
      return answer.id !== answerId
    }))
    Vue.set(state.questionDetails[questionId], 'answers', state.questionDetails[questionId].answers.filter(answer => {
      return answer.id !== answerId
    }))
  },
  [SET_PASSING] (state, passing) {
    // console.log('Kek')
    // console.log(passing)
    state.passing = passing
  },
  [SET_PASSING_TO_TEST] (state, payload) {
    var testId = payload.testId
    var passing = payload.passing
    var testIndex = -1
    for (var i = 0; i < state.tests.length; ++i) {
      if (state.tests[i].id === testId) {
        testIndex = i
      }
    }
    Vue.set(state.tests[testIndex], 'passing', passing)
  },
  [SET_COURSE_TO_TEST] (state, payload) {
    var test = payload.quiz
    var course = payload.course
    var id = payload.id
    if (!state.courseToTests[test]) {
      Vue.set(state.courseToTests, test, {})
    }
    Vue.set(state.courseToTests[test], course, id)
  }
}

const actions = {
  createNote ({ commit }, noteData) {
    Note.create(noteData).then(note => {
      commit(ADD_NOTE, note)
    })
  },
  deleteNote ({ commit }, note) {
    Note.delete(note).then(response => {
      commit(REMOVE_NOTE, note)
    })
  },
  getNotes ({ commit }) {
    Note.list().then(notes => {
      commit(SET_NOTES, { notes })
    })
  },
  registerUser ({ commit }, userData) {
    return User.create(userData).then(user => {
      commit(ADD_USER, user)
    }).catch(function (error) {
      return Promise.reject(error)
    })
  },
  getUsers ({ commit }) {
    User.list().then(users => {
      commit(SET_USERS, { users })
    })
  },
  loginUser ({ commit }, userData) {
    return User.login(userData).then(resp => {
      localStorage.setItem('token', resp['data']['token'])
      console.log(JSON.stringify(resp['data']['user']))
      localStorage.setItem('userInfo', JSON.stringify(resp['data']['user']))
      commit(LOGIN_USER, resp['data']['user'])

      return resp
    }).catch(err => {
      return Promise.reject(err)
    })
  },
  logoutUser ({ commit }) {
    localStorage.removeItem('token')
    localStorage.removeItem('userInfo')
    commit(LOGOUT_USER)
  },
  getUserDetails ({ commit }, id) {
    User.details(id).then(response => {
      var payload = {
        key: id,
        value: response
      }
      commit(ADD_USER_DETAILS, payload)
    })
  },
  createTest ({ commit }, testData) {
    Test.create(testData).then(test => {
      commit(ADD_TEST, test)
    })
  },
  getTests ({ commit, dispatch }) {
    Test.list().then(tests => {
      commit(SET_TESTS, { tests })
      for (var i = 0; i < tests.length; ++i) {
        dispatch('getLastPassing', tests[i].id)
      }
    })
  },
  getTestDetails ({ commit, dispatch }, id) {
    Test.details(id).then(response => {
      var payload = {
        key: id,
        value: response
      }
      commit(ADD_TEST_DETAILS, payload)
      commit(SET_GIVEN_ANSWERS, id)
      dispatch('getCourseToTests')
    })
  },
  createQuestion ({ commit, dispatch }, questionData) {
    Question.create(questionData).then(question => {
      commit(ADD_QUESTION, question)
      dispatch('getTestDetails', question.quiz)
    })
  },
  getQuestions ({ commit }) {
    Question.list().then(questions => {
      commit(SET_QUESTIONS, { questions })
    })
  },
  getQuestionDetails ({ commit }, id) {
    Question.details(id).then(response => {
      var payload = {
        key: id,
        value: response
      }
      commit(ADD_QUESTION_DETAILS, payload)
    })
  },
  createAnswer ({ commit, dispatch }, payload) {
    var questionId = payload.questionId
    var answerData = payload.answerData
    console.log(questionId)
    console.log(answerData)
    Answer.create(answerData).then(answer => {
      dispatch('addAnswerToQuestion', {
        'questionId': questionId,
        'answerId': answer.id
      })
      commit(ADD_ANSWER, answer)
    })
  },
  getAnswers ({ commit }) {
    Answer.list().then(answers => {
      commit(SET_ANSWERS, { answers })
    })
  },
  addAnswerToQuestion ({ dispatch }, payload) {
    var questionId = payload.questionId
    var answerId = payload.answerId
    Question.addAnswerToQuestion(questionId, answerId).then(response => {
      dispatch('getQuestionDetails', questionId)
    })
  },
  addUserToTest ({ commit }, payload) {
    Test.addUserToTest(payload).then(response => {})
  },
  getStudents ({ commit }) {
    User.studentList().then(students => {
      commit(SET_STUDENTS, { students })
      commit(SET_STUDENTS_DICTIONARY)
    })
  },
  addAnswerByUser ({ commit }, payload) {
    Answer.addAnswerToPassing(payload).then(response => {
      commit(ADD_ANSWER_BY_USER, payload)
      // console.log(response)
      commit(ADD_ID_TO_GIVEN_ANSWERS, response)
    })
  },
  deleteAnswerByUser ({ commit }, id) {
    Answer.deleteAnswerToPassing(id).then(response => {
      commit(REMOVE_ANSWER_BY_USER, id)
    })
  },
  getTestResults ({ commit }) {
    Passing.list().then(results => {
      commit(SET_TEST_RESULTS, results)
    })
  },
  removeTestResults ({ commit }, payload) {
    var testId = payload.testId
    var resultId = payload.resultId
    Test.deleteResults(resultId).then(response => {
      commit(REMOVE_TEST_RESULT, testId)
    })
  },
  getGroups ({ commit }) {
    Group.list().then(groups => {
      commit(SET_GROUPS, { groups })
      commit(SET_GROUPS_DICTIONARY)
    })
  },
  addGroupToTest ({ commit }, payload) {
    Test.addGroupToTest(payload).then(response => {})
  },
  getCourses ({ commit }) {
    Course.list().then(courses => {
      commit(SET_COURSES, { courses })
      commit(SET_COURSES_DICTIONARY)
    })
  },
  addCourseToTest ({ commit, dispatch }, payload) {
    Test.addCourseToTest(payload).then(response => {
      // console.log('allah')
      commit(SET_COURSE_TO_TEST, response)
      dispatch('getTestDetails', response.quiz)
    })
  },
  deleteCourseToTest ({ dispatch }, payload) {
    var id = payload.id
    var test = payload.test
    Test.deleteCourseToTest(id).then(response => {
      // commit(SET_COURSE_TO_TEST, response)
      dispatch('getTestDetails', test)
    })
  },
  deleteTest ({ commit }, testId) {
    Test.delete(testId).then(response => {
      commit(REMOVE_TEST, testId)
    })
  },
  deleteQuestion ({ commit }, payload) {
    Question.delete(payload.questionId).then(response => {
      commit(REMOVE_QUESTION, payload)
    })
  },
  deleteAnswer ({ commit }, payload) {
    Answer.delete(payload.answerId).then(response => {
      commit(REMOVE_ANSWER, payload)
    })
  },
  getCurrentPassing ({ commit }, passingData) {
    Passing.create(passingData).then(passing => {
      // console.log(passing)
      commit(SET_PASSING, passing)
    })
  },
  getCurrentPassingDetails ({ commit }, id) {
    Passing.details(id).then(passing => {
      commit(SET_PASSING, passing)
    })
  },
  stopPassing ({ commit }, id) {
    Passing.stop(id).then(passing => {
      commit(SET_PASSING, passing)
    })
  },
  getLastPassing ({ commit }, testId) {
    Passing.last(testId).then(passing => {
      var payload = {
        'testId': testId,
        'passing': passing
      }
      console.log(payload)
      commit(SET_PASSING_TO_TEST, payload)
      // commit(SET_PASSING, passing)
    })
  },
  getCourseToTests ({ commit }) {
    Test.getCourseToTests().then(response => {
      for (var i = 0; i < response.length; ++i) {
        var payload = {
          'quiz': response[i].quiz,
          'course': response[i].course,
          'id': response[i].id
        }
        commit(SET_COURSE_TO_TEST, payload)
      }
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
