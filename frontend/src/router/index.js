import Router from 'vue-router'
import Start from '../components/Start'
import TestInfo from '../components/Tests/TestInfo'
import QuestionInfo from '../components/Questions/QuestionInfo'
import store from '../store'
import { UserType } from '../enums/userType'

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
      beforeEnter: (to, from, next) => {
        if (store.state.userInfo.type === UserType.TEACHER.toString()) {
          next()
        }
      }
    },
    {
      path: '/questionInfo/:id',
      name: 'QuestionInfo',
      component: QuestionInfo,
      beforeEnter: (to, from, next) => {
        if (store.state.userInfo.type === UserType.TEACHER.toString()) {
          next()
        }
      }
    }
  ]
})
