import { HTTP } from './common'

export const User = {
  create (config) {
    return HTTP.post('/rest-auth/registration/', config).then(response => {
      return response
    })
  },
  list () {
    return HTTP.get('/users/').then(response => {
      return response.data
    })
  },
  login (config) {
    return HTTP.post('/rest-auth/login/', config).then(response => {
      return response
    })
  },
  details (id) {
    return HTTP.get('/user/' + id + '/').then(response => {
      return response.data
    })
  }
}
