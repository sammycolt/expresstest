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
        Passing.last(to.params.id).then(response => {
          console.log('!', response)
          if (response.quiz) {
            var id = response.id
            Passing.details(id).then(response => {
              // console.log(response.attempt)
              // console.log(response.quiz)
              // console.log(store.state.tests[response.quiz].max_attempts)
              if (response.is_going === false) {
                console.log('?!', response)
                var testIndex = -1
                for (var i = 0; i < store.state.tests.length; ++i) {
                  if (store.state.tests[i].id === response.quiz) {
                    testIndex = i
                  }
                }
                if (response.attempt < store.state.tests[testIndex].max_attempts) {
                  const answer = window.confirm('Are you sure you want to take the test? If you have already passed it, ' +
                    'the previous result will be deleted!')
                  if (answer) {
                    next()
                  } else {
                    next(false)
                  }
                } else {
                  alert('You have run out')
                }
              } else {
                // console.log('HERE12123')
                next()
              }
            })
          } else {
            // console.log('Kek')
            next()
          }
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
