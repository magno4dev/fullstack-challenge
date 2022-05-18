import axios from 'axios';
import Api from '@/api_config/Api';
export default class CustomerService {

    getCustomersSmall() {
        return axios.get('assets/demo/data/customers-small.json').then(res => res.data.data);
    }

    getCustomersMedium() {
        return axios.get('assets/demo/data/customers-medium.json').then(res => res.data.data);
    }

    getCustomersLarge() {
        return axios.get('assets/demo/data/customers-large.json').then(res => res.data.data);
    }

    getCustomersXLarge() {
        return axios.get('assets/demo/data/customers-xlarge.json').then(res => res.data.data);
    }
    getPedidosPacientes() {
        return Api.get('pedidos_de_analise').then(res => res.data);
    }
    getPedidosAPP() {
        return Api.get('RequestFromAPP').then(res => res.data);
    }
    getAmostrasRecolhidas() {
        return Api.get('amostra_recolhida').then(res => res.data.data);
    }

    // Retorna o método da api para lista de users.
    getListaUtilizadores(){
        return Api.get('lista_utilizadores').then(res=> res.data.data);
    }

}