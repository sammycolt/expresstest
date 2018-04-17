import { HTTP, getHeaders } from './common'

export const Answer = {
  create (config) {
    console.log(config)
    return HTTP.post('/answers/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/answers/', getHeaders()).then(response => {
      return response.data
    })
  }
}
