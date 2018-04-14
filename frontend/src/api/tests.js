import { HTTP } from './common'

export const Test = {
  create (config) {
    return HTTP.post('/tests/', config).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/tests/').then(response => {
      return response.data
    })
  },
  details (id) {
    return HTTP.get('/test/' + id + '/').then(response => {
      return response.data
    })
  }
}
