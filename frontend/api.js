
const axios = require('axios');
// const BASE_URL ="http://13.66.196.147:5000/"
const BASE_URL ="http://0.0.0.0:5000/"

const instance = axios.create({
    baseURL: BASE_URL,
    timeout: 20000
  });

const SIGN_IN =async (email,password)=>{
    const {data} = await instance.post('login',{
        email,
        password
    })
    return data

}

const SIGN_UP =async (cust_name,credential,cust_email,cust_phone)=>{

    const {data} = await instance.post('signup',{
        cust_name,
        credential,
        cust_email,
        cust_phone
    })
    return data
}

const SEARCH_STORES = async (latitude, longitude, radius) => {
    const { data } = await instance.post('searchRestaurantByLatLng', {
        latitude,
        longitude,
        radius
    })
    return data
}

const PLACE_ORDER =async (order_quantity, cust_id, rID)=>{

    const {data} = await instance.post('placeOrder',{
        order_quantity,
        cust_id,
        rID
    })

    return data   
}


export {SIGN_IN,SIGN_UP,SEARCH_STORES,PLACE_ORDER};