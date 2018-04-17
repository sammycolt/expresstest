import { HTTP, getHeaders } from './common'

export const Question = {
  create (config) {
    return HTTP.post('/questions/', config, getHeaders()).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/questions/', getHeaders()).then(response => {
      return response.data
    })
  },
  details (id) {
    return HTTP.get('/question/' + id + '/', getHeaders()).then(response => {
      return response.data
    })
  },
  addAnswerToQuestion (questionId, answerId) {
    var payload = {
      'answer': answerId,
      'question': questionId
    }
    return HTTP.post('/answer_to_question/', payload, getHeaders()).then(response => {
      return response.data
    })
  }
}
