import Api from '@/api_config/Api';

export default class OrderService {

    getListaPedidos() {
        return Api.get('orders/').then(res => res.data);
    }

    getCategoria() {
        return Api.get('categories/').then(res => res.data);

    }
}