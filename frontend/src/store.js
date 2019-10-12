import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    departureLocation: '',
    destination: '',
    tripInterval: []
  },
  mutations: {
    updateDeparture(state, departureLocation) {
      state.departureLocation = departureLocation
    },
    updateDestination(state, destination) {
      state.destination = destination
    },
    updateTripInterval(state, tripInterval) {
      state.tripInterval = tripInterval
    },
  },
  actions: {

  }
})
