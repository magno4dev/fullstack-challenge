//import Api from '@/api_config/Api'
import axios from 'axios';

//const END_POINT_PATIENTS = 'pacientes';

export default {

    namespaced: true,
    state: {
        patientInfo: {}
    },
    getters: {

        dataPatient(state) {
            return state.patientInfo;
        },

    },
    mutations: {

        SET_PATIENT(state, patientInfo) {
            state.patientInfo = patientInfo;
        },
    },
    actions: {
        async patients({ commit }) {

            let den = await axios.get('http://45.61.53.39/elab/public/api/pacientes')
            console.log(den.data.data);
            commit("SET_PATIENT", den.data);
        }
    }
}