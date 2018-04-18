import { HTTP, getHeaders } from './common'

export const User = {
  create (config) {
    return HTTP.post('/rest-auth/registration/', config).then(response => {
      return response
    })
  },
  list () {
    return HTTP.get('/users/', getHeaders()).then(response => {
      return response.data
    })
  },
  login (config) {
    return HTTP.post('/rest-auth-jwt/login/', config).then(response => {
      return response
    })
  },
  details (id) {
    return HTTP.get('/user/' + id + '/', getHeaders()).then(response => {
      return response.data
    })
  },
  studentList () {
    return HTTP.get('/students/', getHeaders()).then(response => {
      return response.data
    })
  }
}
