import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/v1/'
  // withCredentials: true
})

export function getHeaders () {
  return {
    headers: {'Authorization': 'JWT ' + localStorage.getItem('token')}
  }
}
