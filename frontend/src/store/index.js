import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import { User } from '../api/users'
import {
  ADD_NOTE,
  REMOVE_NOTE,
  SET_NOTES,
  ADD_USER,
  SET_USERS,
  LOGIN_USER,
  LOGOUT_USER
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  notes: [],
  users: [],
  isLogged: !!localStorage.getItem('token'),
  userInfo: localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo')) : {}
}

const getters = {
  notes: state => state.notes,
  users: state => state.users,
  isLogged: state => state.isLogged,
  userInfo: state => state.userInfo
}

const mutations = {
  [ADD_NOTE] (state, note) {
    state.notes = [note, ...state.notes]
  },
  [REMOVE_NOTE] (state, { id }) {
    state.notes = state.notes.filter(note => {
      return note.id !== id
    })
  },
  [SET_NOTES] (state, { notes }) {
    state.notes = notes
  },
  [ADD_USER] (state, user) {
    state.users = [user, ...state.users]
  },
  [SET_USERS] (state, { users }) {
    state.users = users
  },
  [LOGIN_USER] (state, userInfo) {
    state.isLogged = true
    state.userInfo = userInfo
  },

  [LOGOUT_USER] (state) {
    state.isLogged = false
    state.userInfo = {}
  }

}

const actions = {
  createNote ({ commit }, noteData) {
    Note.create(noteData).then(note => {
      commit(ADD_NOTE, note)
    })
  },
  deleteNote ({ commit }, note) {
    Note.delete(note).then(response => {
      commit(REMOVE_NOTE, note)
    })
  },
  getNotes ({ commit }) {
    Note.list().then(notes => {
      commit(SET_NOTES, { notes })
    })
  },
  registerUser ({ commit }, userData) {
    return User.create(userData).then(user => {
      commit(ADD_USER, user)
    }).catch(function (error) {
      return Promise.reject(error)
    })
  },
  getUsers ({ commit }) {
    User.list().then(users => {
      commit(SET_USERS, { users })
    })
  },
  loginUser ({ commit }, userData) {
    return User.login(userData).then(resp => {
      localStorage.setItem('token', resp['data']['token'])
      localStorage.setItem('userInfo', JSON.stringify(resp['data']['user']))
      commit(LOGIN_USER, resp['data']['user'])

      return resp
    }).catch(err => {
      return Promise.reject(err)
    })
  },
  logoutUser ({ commit }) {
    localStorage.removeItem('token')
    localStorage.removeItem('userInfo')
    commit(LOGOUT_USER)
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
