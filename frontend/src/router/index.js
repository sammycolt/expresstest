import Router from 'vue-router'
import Start from '../components/Start'
import TestInfo from '../components/TestInfo'

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
    }
  ]
})
