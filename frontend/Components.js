import React, { useState, useEffect,useContext } from 'react';
import { Button, View, TextInput, Text, Pressable, Touchable, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import GoogleMapReact from 'google-map-react';
import AppContext from './AppContext';
import Toast from 'react-native-toast-message';
import { Feather } from '@expo/vector-icons';
import styles from './styles';
import { Foundation } from '@expo/vector-icons'; 
import NumericInput from 'react-native-numeric-input'
import { useNavigation } from '@react-navigation/native'

import {PLACE_ORDER,SEARCH_STORES,SEARCH_POPULAR,STORE_REPORT} from './api';
import {Collapse,CollapseHeader, CollapseBody, AccordionList} from 'accordion-collapse-react-native';



const StoreDetail = ({ route, navigation }) => {
    const [orderQuantity, setOrderQuantity] = useState(1)


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
                text1: 'Success',
                text2: 'Order placed!'
            })
        )

    }

    return (
        <View style={styles.detailContainer}>
            <View style={{ height: "50px" }}>
                <Text>
                    Name: {name}
                </Text>
            </View>
            <View style={{ height: "50px" }}>
                <Text>
                    Cuisine: {cuisine}
                </Text>
            </View>
            <View style={{ height: "50px" }}>
                <Text>
                    Rating: {rating}
                </Text>
            </View>
            <View style={{ height: "50px" }}>
                <Text>
                    Phone Number: {phone}
                </Text>
            </View>
            <View style={{ height: "50px" }}>
                <Text>
                    Remaining quantity: {quantity}
                </Text>
            </View>
            <View styles={{
                height: "180px",
            }}>
                <Text >
                    Place order - Number of quantity:
                </Text>

            </View>
            <View styles={{
                flexDirection: "column",
                alignContent: 'center',
                paddingTop: "50px",
                width: "100%"
            }}>
                <NumericInput type='up-down'
                styles={{
                    width: "20%"
                }}
                    minValue={1}
                    maxValue={quantity}
                    value={orderQuantity}
                    onChange={setOrderQuantity} />
                <TouchableOpacity
                    onPress={() => placeOrder(orderQuantity)}
                    style={styles.plcBtn}>
                    <Text style={styles.loginText}>Place Order</Text>
                </TouchableOpacity>
            </View>

        </View>
    )
}


const StoreReport = (props) => {
    const [report, setReport] = useState([])
    useEffect(() => {
        const loadReport = async () => {
            //API: store list
            const data = await STORE_REPORT(3,2021)
            setReport(data)
        }

        loadReport()

    }, [])

    const StoreItem = (datum) => (<TouchableOpacity
        style={{
            flexDirection: 'column',
            alignContent: 'center'
        }}
        key={datum.name}
         >
        <View>
            <Text>
                Name: {datum.name} 
                
            </Text>
        </View>
        <View>
            <Text>
                Orders: {datum.order}
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
            data={report}
            renderItem={renderItem}
            keyExtractor={item => item.name}
        />    
    </View>)
}

const StoreListView = (props) => {
    const { navigation} = props

    useEffect(() => {
        navigation.setOptions({
            headerRight: () => (
                
                <TouchableOpacity
                    style={{
                        alignItems: 'center',
                        backgroundColor: '#FFF',
                        padding: 10
                    }}
                    onPress={() => {
                        console.log(navigation)
                        navigation.navigate("Store Report")
                    }}>
                    <Text> Store Report </Text>
                </TouchableOpacity>
            ),
        });
    })
    const { state } = useContext(AppContext);
    
    const {location:{lat,lng}} = state

    const [firstExpanded, setFirstExpanded] = useState(true)

    const [stores, setStores] = useState([])
    const [populars, setPopulars] = useState([])
    useEffect(() => {
        const loadData = async () => {
            //API: store list
            const stores = await SEARCH_STORES(lat,lng,10000)
            setStores(stores)
        }
        const loadPopulars = async () => {
            //API: store list
            const pop = await SEARCH_POPULAR(lat,lng,10000)
            setPopulars(pop)
        }
        loadData()
        loadPopulars()

    }, [])

    const StoreItem = (store) => (<TouchableOpacity
        style={styles.listItem}
        lat={store.lat}
        lng={store.lng}
        key={store.id}
        onPress={() => props.navigation.navigate('Store Detail', store)} >
        <View style={{
            flexDirection: 'column',
            alignContent: 'center'
        }}>
            <View
                style={{
                    flexDirection: 'row',
                    alignContent: 'center'
                }} >
            <Text style={{ width: "50%", height:"30px" }}>
                Name: {store.name}
            </Text>
            <Text style={{ width: "50%", height:"30px"}}>
                Cuisine: {store.cuisine}
            </Text>
        </View>
        <View
            style={{
                flexDirection: 'row',
                alignContent: 'center'
            }}>
            <Text style={{ width: "50%" }}>
                Address: {store.address}
            </Text>
            <Text style={{ width: "50%" }}>
                Distance: {store.distance / 1000}km
            </Text>
        </View>
        </View>
    </TouchableOpacity >)

    const renderItem = ({ item }) => (
        <StoreItem {...item} />
    );
    // TODO: fetch store list from server
    return (<View style={styles.listPage}>
        <Collapse isExpanded={firstExpanded} 
            
            onToggle={() => setFirstExpanded(!firstExpanded)}>
            <CollapseHeader>
                <View>
                    <Text>Nearest Stores</Text>

                </View>
            </CollapseHeader>
            <CollapseBody>
            <FlatList
                    style={styles.listContainer}
                    data={stores}
                    renderItem={renderItem}
                    keyExtractor={item => item.id}
                /> 

                     </CollapseBody>
        </Collapse>
        <Collapse isExpanded={!firstExpanded}
            style={{flex:1}}
            onToggle={() => setFirstExpanded(!firstExpanded)}>
            <CollapseHeader>
                <View>

                    <Text>Most Popular</Text>
                </View>
            </CollapseHeader>
            <CollapseBody>
                <FlatList
                    style={styles.listContainer}
                    data={populars}
                    renderItem={renderItem}
                    keyExtractor={item => item.id}
                />
            </CollapseBody>
        </Collapse>


    </View>)
}

const StoreMapView = (props) => {
    const defaultProps = {
        zoom:13
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
    StoreReport
}
