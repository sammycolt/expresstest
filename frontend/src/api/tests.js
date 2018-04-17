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
  }
}
