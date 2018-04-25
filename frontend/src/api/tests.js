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
  deleteResults (resultId) {
    return HTTP.delete(`/results/${resultId}/`, getHeaders()).then(response => {
      return response.data
    })
  },
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
  }
}
