import Router from 'vue-router'
import Start from '../components/Start'
import TestInfo from '../components/Tests/TestInfo'
import QuestionInfo from '../components/Questions/QuestionInfo'
import TestPassing from '../components/TestPassing/TestPassing'
import store from '../store'
import { UserType } from '../enums/userType'

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
      beforeEnter: (to, from, next) => studentsOutZone(to, from, next)
    },
    {
      path: '/questionInfo/:id',
      name: 'QuestionInfo',
      component: QuestionInfo,
      beforeEnter: (to, from, next) => studentsOutZone(to, from, next)
    },
    {
      path: '/passing/:id',
      name: 'TestPassing',
      component: TestPassing
    }
  ]
})
