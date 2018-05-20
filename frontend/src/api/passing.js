import { HTTP, getHeaders } from './common'

export const Passing = {
  list () {
    return HTTP.get('/passing/', getHeaders()).then(response => {
      return response.data
    })
  },
  create (config) {
    return HTTP.post('/passing/', config, getHeaders()).then(response => {
      // console.log(response)
      return response.data
    })
  },
  details (id) {
    return HTTP.get('/passing_details/' + id + '/', getHeaders()).then(response => {
      return response.data
    })
  }
}