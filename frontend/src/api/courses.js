import { HTTP, getHeaders } from './common'

export const Course = {
  create (config) {
    return HTTP.post('/courses/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/courses/', getHeaders()).then(response => {
      return response.data
    })
  }
}
