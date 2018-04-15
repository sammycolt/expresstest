import Router from 'vue-router'
import Start from '../components/Start'
import TestInfo from '../components/Tests/TestInfo'
import QuestionInfo from '../components/Questions/QuestionInfo'

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
      component: TestInfo
    },
    {
      path: '/questionInfo/:id',
      name: 'QuestionInfo',
      component: QuestionInfo
    }
  ]
})
