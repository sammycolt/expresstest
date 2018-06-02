import { HTTP, getHeaders } from './common'

export const Answer = {
  create (config) {
    // console.log(config)
    return HTTP.post('/answers/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/answers/', getHeaders()).then(response => {
      return response.data
    })
  },
  // addAnswerByUser (config) {
  //   return HTTP.post('/answer_by_user/', config, getHeaders()).then(response => {
  //     return response.data
  //   })
  // },
  addAnswerToPassing (config) {
    return HTTP.post('/answer_to_passing/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  deleteAnswerToPassing (answerToPassing) {
    return HTTP.delete(`/answer_to_passing/${answerToPassing}/`, getHeaders()).then(response => {
      return response.data
    })
  },
  // deleteAnswerByUser (answerByUser) {
  //   return HTTP.delete(`/answer_by_user/${answerByUser}/`, getHeaders()).then(response => {
  //     return response.data
  //   })
  // },
  delete (id) {
    return HTTP.delete(`/answers/${id}/`, getHeaders()).then(response => {
      return response.data
    })
  }
}
