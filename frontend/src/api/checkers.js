import { HTTP, getHeaders } from './common'

export const Checker = {
  create (config) {
    return HTTP.post('/checker/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  delete (id) {
    return HTTP.delete(`/my_checker/${id}/`, getHeaders()).then(response => {
      return response.data
    })
  },
  otherCheckers () {
    return HTTP.get('/checker/', getHeaders()).then(response => {
      return response.data
    })
  },
  myCheckers () {
    return HTTP.get('/my_checker/', getHeaders()).then(response => {
      return response.data
    })
  }

}
