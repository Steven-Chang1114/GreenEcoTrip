import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    departureLocation: '',
    destination: '',
    tripInterval: new Date(),
    trips: [
    {
      id: 0,
      carbon: 69,
      price: 420,
      steps: [
      {id: 0, start: "Barcelona", end: "London", type: "flight"},
      {id: 1, start: "London", end: "Edinburgh", type: "rail"}
    ]},
    {
      id: 1,
      carbon: 9,
      price: 4567890,
      steps: [
      {id: 0, start: "Barcelona", end: "Valencia", type: "flight"},
      {id: 1, start: "Valencia", end: "London", type: "rail"}
    ]},
    {
      id: 1,
      carbon: 4353,
      price: 1,
      steps: [
      {id: 0, start: "Madrid", end: "Valencia", type: "bus"},
      {id: 1, start: "Valencia", end: "Barcelona", type: "flight"},
      {id: 2, start: "Barcelona", end: "London", type: "rail"},
      {id: 3, start: "London", end: "KL", type: "rail"}
    ]},
    ]
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
    updateTrips(state, trips) {
      state.trips = trips
    }
  },
  actions: {

  }
})
