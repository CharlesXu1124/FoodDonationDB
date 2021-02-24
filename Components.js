import React, { useState, useEffect } from 'react';
import { Button, View, TextInput, Text, Pressable, Touchable, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import GoogleMapReact from 'google-map-react';
import AppContext from './AppContext';
import Toast from 'react-native-toast-message';
import { Feather } from '@expo/vector-icons';
import styles from './styles';
import { Foundation } from '@expo/vector-icons'; 

const StoreDetail = ({ route, navigation }) => {
    console.log(route, navigation)
    //TODO: API: store detail? or just use the data from list

    const { params: { name } } = route
    return (
        <View style={styles.container}>
            <Text>
                Hey {name}
            </Text>
            <TouchableOpacity
                onPress={() => navigation.navigate('Place Order')}
                style={styles.loginBtn}>
                <Text style={styles.loginText}>Place Order</Text>
            </TouchableOpacity>
        </View>
    )
}

const PlaceOrder = ({ route, navigation }) => {
    console.log(route, navigation)
    //TODO: API: place order
    // const { params: { store } } = route

    const placeOrder = () => {
        Toast.show({
            text1: 'Hello',
            text2: 'This is some something 👋'
        });
        navigation.goBack()
    }

    return (
        <View >
            <Pressable
                onPress={placeOrder}>
                <Text>
                    Place Order
            </Text>

            </Pressable>
        </View>
    )
}

const StoreListView = (props) => {
    const [stores, setStores] = useState([])
    useEffect(() => {
        const loadData = async () => {
            //TODO: API: store list

            setStores(
                [{
                    name: "name2",
                    lat: 59.95,
                    lng: 30.33,
                    id: "123123"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345246"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345244"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345243"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345242"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345241"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "23452555"
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "23452455"
                }, {
                    name: "name5",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "234524622"
                }, {
                    name: "name1",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "2345234622"
                }, {
                    name: "name4",
                    lat: 59.961,
                    lng: 30.3409,
                    id: "145234622"
                }]
            )
        }
        loadData()
    }, [])


    const StoreItem = ({ lat, lng, id, name, }) => (<TouchableOpacity
        style={styles.listItem}
        lat={lat}
        lng={lng}
        key={id}
        onPress={() => props.navigation.navigate('Store Detail', { name, id, lat, lng })} >
        <View>
            <Text>
                {name}
            </Text>
        </View>
        <View>
            <Text>
                Address abc st
            </Text>
        </View>
        <View>
            <Text>
                Stock: xxxx
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
        center: {
            lat: 59.95,
            lng: 30.33
        },
        zoom: 11
    };

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
            //TODO: API: store list

            setStores(
                [{
                    name: "name2xxxxxxx",
                    lat: 59.95,
                    lng: 30.33,
                    id: 123123
                }, {
                    name: "name3",
                    lat: 59.961,
                    lng: 30.3409,
                    id: 2345246
                }]
            )
        }
        loadData()
    }, [])

    return (
        <View style={{ height: '100%', width: '100%' }}>

            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyAA7iIEFkFfDYAoxIJRFsWjn6OzvhUhwI8' }}
                defaultCenter={defaultProps.center}
                defaultZoom={defaultProps.zoom}>
                {
                    stores.map(store =>
                        <StoreMarker {...store} key={store.id} {...props} />)
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
        <View >
            <Text>
                Find Food!
            </Text>
        </View>
    )
}



export {
    StoreDetail,
    StoreListView,
    StoreMapView,
    SplashScreen,
    PlaceOrder
}
