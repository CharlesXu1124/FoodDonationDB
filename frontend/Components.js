import React, { useState, useEffect,useContext } from 'react';
import { Button, View, TextInput, Text, Pressable, Touchable, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import GoogleMapReact from 'google-map-react';
import AppContext from './AppContext';
import Toast from 'react-native-toast-message';
import { Feather } from '@expo/vector-icons';
import styles from './styles';
import { Foundation } from '@expo/vector-icons'; 
import NumericInput from 'react-native-numeric-input'
import {PLACE_ORDER,SEARCH_STORES} from './api';

const StoreDetail = ({ route, navigation }) => {
    const [orderQuantity, setOrderQuantity] = useState(1)

    console.log(route, navigation)
    const { state } = useContext(AppContext);
    console.log(state);
    const {userToken:{cus_id,cus_name}} = state
    const { params: { name,
        id,
        cuisine,
        phone,
        rating,
        quantity } } = route
    const placeOrder = (quantity) => {
        //API: place order
        PLACE_ORDER(quantity,cus_id,id)
        .then(
            ()=>
            Toast.show({
                text1: 'Hello',
                text2: 'This is some something 👋'
            })
        )

    }

    return (
        <View style={styles.container}>
            <View>
                <Text>
                {name}    
                </Text>
            </View>
            <View>
                <Text>
                Cuisine: {cuisine}    
                </Text>
                <Text>
                {rating}    
                </Text>
            </View>
            <View>
                <Text>
                Phone Number: {phone}    
                </Text>
            </View>
            <View>
                <Text>
                Remaining quantity: {quantity}    
                </Text>
            </View>
            <View>
                <NumericInput type='up-down'
                    minValue={1}
                    maxValue = {quantity} 
                    value={orderQuantity}
                    onChange={setOrderQuantity} />
            </View>
            <TouchableOpacity
                onPress={() => placeOrder(orderQuantity)}
                style={styles.loginBtn}>
                <Text style={styles.loginText}>Place Order</Text>
            </TouchableOpacity>
        </View>
    )
}

const StoreListView = (props) => {
    const { state } = useContext(AppContext);
    const {location:{lat,lng}} = state

    const [stores, setStores] = useState([])
    useEffect(() => {
        const loadData = async () => {
            //API: store list
            const stores = SEARCH_STORES(lat,lng)
            setStores(stores)
        }
        loadData()
    }, [])

    const StoreItem = (store) => (<TouchableOpacity
        style={styles.listItem}
        lat={store.lat}
        lng={store.lng}
        key={store.id}
        onPress={() => props.navigation.navigate('Store Detail', store)} >
        <View>
            <Text>
                {store.name} 
                Cuisine: {store.cuisine} 
            </Text>
        </View>
        <View>
            <Text>
                Address: {store.address}
                Distance: {store.distance/1000}km
            </Text>
        </View>
    </TouchableOpacity>)

    const renderItem = ({ item }) => (
        <StoreItem {...item} />
    );
    // TODO: fetch store list from server
    return (<View style={styles.container}>
        <FlatList
            style={styles.listContainer}
            data={stores}
            renderItem={renderItem}
            keyExtractor={item => item.id}
        />

    </View>)
}

const StoreMapView = (props) => {
    const defaultProps = {
        zoom: 11
    };
    const { state } = useContext(AppContext);
    const {location} = state

    const [stores, setStores] = useState([])

    const StoreMarker = ({ lat, lng, id, name, navigation }) => (<TouchableOpacity
        lat={lat}
        lng={lng}
        key={id}
        style={ styles.storeMarker}
        onPress={() => navigation.navigate('Store Detail', { name, id, lat, lng })} >
            <Foundation style={{paddingBottom:10}} name="marker" size={25} color="#F23" />
            <Text style={{marginLeft:6, fontSize:16, paddingBottom:4}}>
                {name}
            </Text>
    </TouchableOpacity>)

    useEffect(() => {
        const loadData = async () => {
            //TODO:  store list
            const dStores = await SEARCH_STORES(location.lat,location.lng,10000)

            console.log(dStores)

            setStores(dStores)

        }
        loadData()
    }, [])

    return (
        <View style={{ height: '100%', width: '100%' }}>

            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyAA7iIEFkFfDYAoxIJRFsWjn6OzvhUhwI8' }}
                defaultCenter={location}
                defaultZoom={defaultProps.zoom}>
                {
                    stores.length >0 && stores.map(store =>{
                        console.log(store)
                        return (<StoreMarker {...store} key={store.id} {...props} />)})
                }
            </GoogleMapReact>
            <TouchableOpacity
                title='List View'
                style={styles.floating}
                onPress={() => {props.navigation.navigate('Store List')}}>
                <Feather name="list" size={28}
                    backgroundColor="#007AFF" />
            </TouchableOpacity>
        </View>
    );
}

const SplashScreen = (props) => {
    return (
        <View style={styles.container}>
            <Text>
                Find Donation!
            </Text>
        </View>
    )
}



export {
    StoreDetail,
    StoreListView,
    StoreMapView,
    SplashScreen,
}
