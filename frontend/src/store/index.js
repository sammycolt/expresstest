import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import { User } from '../api/users'
import { Test } from '../api/tests'
import { Answer } from '../api/answers'
import { Question } from '../api/questions'
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
  REMOVE_ANSWER_BY_USER
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
  studentsDictionary: {}
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
  studentsDictionary: state => state.studentsDictionary
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
    if (!state.studentsDictionary.length) {
      var students = {}
      for (var i = 0; i < state.students.length; ++i) {
        students[state.students[i].username] = state.students[i]
      }
      Vue.set(state, 'studentsDictionary', students)
    }
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
  getTests ({ commit }) {
    Test.list().then(tests => {
      commit(SET_TESTS, { tests })
    })
  },
  getTestDetails ({ commit }, id) {
    Test.details(id).then(response => {
      var payload = {
        key: id,
        value: response
      }
      commit(ADD_TEST_DETAILS, payload)
      commit(SET_GIVEN_ANSWERS, id)
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
    Answer.addAnswerByUser(payload).then(response => {
      commit(ADD_ANSWER_BY_USER, payload)
      console.log(response)
      commit(ADD_ID_TO_GIVEN_ANSWERS, response)
    })
  },
  deleteAnswerByUser ({ commit }, id) {
    Answer.deleteAnswerByUser(id).then(response => {
      commit(REMOVE_ANSWER_BY_USER, id)
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
