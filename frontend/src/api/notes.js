import { HTTP, getHeaders } from './common'

export const Note = {
  create (config) {
    return HTTP.post('/notes/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  delete (note) {
    return HTTP.delete(`/notes/${note.id}/`, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/notes/', getHeaders()).then(response => {
      return response.data
    })
  }
}
