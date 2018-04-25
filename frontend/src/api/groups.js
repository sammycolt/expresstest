import { HTTP, getHeaders } from './common'

export const Group = {
  create (config) {
    return HTTP.post('/groups/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/groups/', getHeaders()).then(response => {
      return response.data
    })
  },
  addUserToGroup (userId, groupId) {
    var payload = {
      'user': userId,
      'group': groupId
    }
    return HTTP.post('/user_to_group/', payload, getHeaders()).then(response => {
      return response.data
    })
  }
}
