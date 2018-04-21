import axios from 'axios'
import store from '../store/index'
import router from '../router/index'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
  validateStatus: function (status) {
    if (status === 401) {
      store.dispatch('logoutUser')
      router.push({name: 'Start'})
    }
    return status >= 200 && status < 300
  }
})

export function getHeaders () {
  return {
    headers: {'Authorization': 'JWT ' + localStorage.getItem('token')}
  }
}
