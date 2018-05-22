import { HTTP, getHeaders } from './common'
// import axios from 'axios'

export const Test = {
  create (config) {
    return HTTP.post('/tests/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/tests/', getHeaders()).then(response => {
      return response.data
    })
  },
  details (id) {
    return HTTP.get('/test/' + id + '/', getHeaders()).then(response => {
      return response.data
    })
  },
  addUserToTest (payload) {
    return HTTP.post('/user_to_quiz/', payload, getHeaders()).then(response => {
      return response.data
    })
  },
  results () {
    return HTTP.get('/results/', getHeaders()).then(response => {
      return response.data
    })
  },
  // deleteResults (resultId) {
  //   return HTTP.delete(`/results/${resultId}/`, getHeaders()).then(response => {
  //     return response.data
  //   })
  // },
  delete (id) {
    return HTTP.delete(`/tests/${id}`, getHeaders()).then(response => {
      return response.data
    })
  },
  addGroupToTest (payload) {
    return HTTP.post('/quiz_to_group/', payload, getHeaders()).then(response => {
      return response.data
    })
  },
  addCourseToTest (payload) {
    return HTTP.post('/quiz_to_course/', payload, getHeaders()).then(response => {
      return response.data
    })
  },
  deleteCourseToTest (id) {
    return HTTP.delete(`/quiz_to_course/${id}`, getHeaders()).then(response => {
      return response.data
    })
  },
  getCourseToTests () {
    return HTTP.get('/quiz_to_course/', getHeaders()).then(response => {
      return response.data
    })
  },
  deleteGroupToTest (id) {
    return HTTP.delete(`/quiz_to_group/${id}`, getHeaders()).then(response => {
      return response.data
    })
  },
  getGroupToTests () {
    return HTTP.get('/quiz_to_group/', getHeaders()).then(response => {
      return response.data
    })
  },
  deleteUserToTest (id) {
    return HTTP.delete(`/user_to_quiz/${id}`, getHeaders()).then(response => {
      return response.data
    })
  },
  getUserToTests () {
    return HTTP.get('/user_to_quiz/', getHeaders()).then(response => {
      return response.data
    })
  }
}
