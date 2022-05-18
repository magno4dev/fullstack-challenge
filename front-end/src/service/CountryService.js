import axios from 'axios'

export default class CountryService {

    getCountries() {
        return axios.get('assets/demo/data/countriesfff.json').then(res => res.data.data);
    }
}
