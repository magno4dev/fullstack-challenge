import axios from 'axios';

export default class Mydata{
	
	getDataH(){

		//return axios.get('assets/demo/data/myDataH20.json').then(res => res.data.data);


		return axios.get('assets/demo/data/products.json').then(res => res.data.data);
	}	

}