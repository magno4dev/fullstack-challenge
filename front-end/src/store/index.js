import { createStore } from "vuex";

import pacientes from '@/store/modules/operacoes/pacientes'

const store = createStore({
    namespaced: true,
    modules: {
        pacientes
    }
});
export default store;