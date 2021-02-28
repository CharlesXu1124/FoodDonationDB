import { StyleSheet, Text, View } from 'react-native';
import React, {
  useEffect,
  useMemo,
  useReducer,
} from 'react';
import {
  SplashScreen,
  StoreListView,
  StoreMapView,
  StoreDetail
} from './Components';
import{
  SignInScreen,
  SignUpScreen

} from './AuthenticateComponents';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import AsyncStorage from '@react-native-async-storage/async-storage';
import AppContext from './AppContext';
import Toast from 'react-native-toast-message';
import {SIGN_UP, SIGN_IN} from './api'



// const SHOP_LIST = 


const Stack = createStackNavigator();

export default function App() {
  const [state, dispatch] = useReducer(
    (prevState, action) => {
      console.log(action)
      switch (action.type) {
        case 'RESTORE_TOKEN':
          return {
            ...prevState,
            userToken: action.token,
            isLoading: false,
          };
        case 'SIGN_IN':
        case 'SIGN_UP':
          return {
            ...prevState,
            isSignout: false,
            isLoading: false,
            userToken: action.token,
          };
        case 'SIGN_OUT':
          return {
            ...prevState,
            isSignout: true,
            isLoading: false,
            userToken: null,
          };
      }
    },
    {
      isLoading: true,
      isSignout: false,
      userToken: null,
      location:{lat: 47.6239,
        lng: -122.335}
      //TODO: device location

    }
  );

  useEffect(() => {
    async function fetchUser() {
      let userData;
      try {
        userData = await AsyncStorage.getItem('userData')
      } catch (e) {
      }
      dispatch({ type: 'RESTORE_TOKEN', token: JSON.parse(userData) });
    }
    setTimeout(fetchUser, 1000)
  }, [])

  const authContext = useMemo(
    () => ({
      
      signIn: async ({ email, password }) => {
        // API: sign in
        const userData = await SIGN_IN(email, password)
        console.log(userData)

        AsyncStorage.setItem('userData', JSON.stringify(userData))

        dispatch({ type: 'SIGN_IN', token: userData });
      },
      signOut: () => {
        AsyncStorage.setItem('userData', null)
        dispatch({ type: 'SIGN_OUT' })
      },
      signUp: async ({ username, password,email,phone })  => {
        
        // API: sign up
        const userData = await SIGN_UP(username, password,email,phone)
        console.log(userData)
        
        AsyncStorage.setItem('userData', JSON.stringify(userData))

        dispatch({ type: 'SIGN_UP', token: userData });
      },
    }),
    []
  );

  if (state.isLoading) {
    // We haven't finished checking for the token yet
    return <SplashScreen />
  }
  return (
    <AppContext.Provider value={{authContext,state}}>
      <NavigationContainer>
        {state.userToken ?
          <Stack.Navigator>
            <Stack.Screen name="Home" component={StoreMapView} />
            <Stack.Screen name="Store List" component={StoreListView} />
            <Stack.Screen name="Store Detail" component={StoreDetail} />

          </Stack.Navigator>
          :
          <Stack.Navigator>
            <Stack.Screen name="Sign In" component={SignInScreen} />
            <Stack.Screen name="Sign Up" component={SignUpScreen} />
          </Stack.Navigator>
        }
        <Toast ref={(ref) => Toast.setRef(ref)} />
      </NavigationContainer>
    </AppContext.Provider>
  );
}
