import { HTTP } from './common'

export const Question = {
  create (config) {
    return HTTP.post('/questions/', config).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/questions/').then(response => {
      return response.data
    })
  }
}
