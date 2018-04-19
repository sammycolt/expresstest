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
  }
}
