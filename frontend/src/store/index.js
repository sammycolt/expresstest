import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import { User } from '../api/users'
import {
  ADD_NOTE,
  REMOVE_NOTE,
  SET_NOTES,
  ADD_USER,
  SET_USERS
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  notes: [],
  users: [],
  isAutintificated: false
}

const getters = {
  notes: state => state.notes,
  users: state => state.users
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
    return User.login(userData).then(response => {
      return response
    }).catch(err => {
      return Promise.reject(err)
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
