import Router from 'vue-router'
import Start from '../components/Start'
import TestInfo from '../components/Tests/TestInfo'
import QuestionInfo from '../components/Questions/QuestionInfo'
import TestPassing from '../components/TestPassing/TestPassing'
import store from '../store'
import { UserType } from '../enums/userType'
import { Passing } from '../api/passing'
import StudentTestResultsInDetail from '../components/TestPassing/StudentTestResultsInDetail'

function studentsOutZone (to, from, next) {
  if (store.state.userInfo.type === UserType.TEACHER.toString()) {
    next()
  }
}

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start
    },
    {
      path: '/testInfo/:id',
      name: 'TestInfo',
      component: TestInfo,
      beforeEnter (to, from, next) {
        studentsOutZone(to, from, next)
      }
    },
    {
      path: '/questionInfo/:id:testId',
      name: 'QuestionInfo',
      component: QuestionInfo,
      beforeEnter: (to, from, next) => studentsOutZone(to, from, next)
    },
    {
      path: '/passing/:id',
      name: 'TestPassing',
      component: TestPassing,
      beforeEnter (to, from, next) {
        Passing.last().then(response => {
          var id = response[0].id
          Passing.details(id).then(response => {
            console.log(response)
            if (response.is_going === false) {
              const answer = window.confirm('Are you sure you want to take the test? If you have already passed it, ' +
                'the previous result will be deleted!')
              if (answer) {
                next()
              } else {
                next(false)
              }
            } else {
              next()
            }
          })
        })
      }
    },
    {
      path: '/results/:id',
      name: 'TestResults',
      component: StudentTestResultsInDetail
    }
  ]
})
