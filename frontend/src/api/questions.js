import { HTTP } from './common'

export const Question = {
  create (config) {
    return HTTP.post('/questions/', config).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/questions/').then(response => {
      return response.data
    })
  },
  details (id) {
    return HTTP.get('/question/' + id + '/').then(response => {
      return response.data
    })
  },
  addAnswerToQuestion (questionId, answerId) {
    var payload = {
      'answer': answerId,
      'question': questionId
    }
    return HTTP.post('/answer_to_question/', payload).then(response => {
      return response.data
    })
  }
}
