import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    departureLocation: '',
    destination: '',
    departureTime: '',
    arrivalTime: '',
  },
  mutations: {
    updateDeparture(state, departureLocation) {
      state.departureLocation = departureLocation
    },
    updateDestination(state, destination) {
      state.destination = destination
    },
    updateDepartTime(state, departureTime) {
      state.departureTime = departureTime
    },
    updateArrivalTime(state, arrivalTime) {
      state.arrivalTime = arrivalTime
    }
  },
  actions: {

  }
})
