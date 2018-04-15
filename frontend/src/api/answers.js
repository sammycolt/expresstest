import { HTTP } from './common'

export const Answer = {
  create (config) {
    console.log(config)
    return HTTP.post('/answers/', config).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/answers/').then(response => {
      return response.data
    })
  }
}
