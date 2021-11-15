import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
    todoMovies: [],
    randomMovie: null
  },
  getters: {
    randomMovie(state) {
      return state.randomMovie
    }
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MOVIE: function(state, todoMovie){
      state.todoMovies.push(todoMovie)
    },
    PICK_RANDOM_MOVIE: function (state, randomMovie) {
      state.randomMovie = randomMovie
    }
  },
  actions: {
    LoadMovieCards: function({commit}){
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: process.env.VUE_APP_TMDB_API_KEY,
          language: 'ko-KR',
        }
      })
        .then(res => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    },
    pickRandomMovie({ commit }, state) {
      const randomMovie = _.sample(state.movieCards)
      commit('PICK_RANDOM_MOVIE', randomMovie)
    },
    createMovie: function({commit}, todoMovie){
      commit('CREATE_MOVIE', todoMovie)
    },
  },
  modules: {
  }
})
