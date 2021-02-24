import { StyleSheet, Text, View } from 'react-native';
import React, {
  Component,
  useState,
  useEffect,
  useMemo,
  useReducer,
  createContext
} from 'react';
import {
  SplashScreen,
  StoreListView,
  StoreMapView,
  StoreDetail,
  PlaceOrder
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
          return {
            ...prevState,
            isSignout: false,
            userToken: action.token,
          };
        case 'SIGN_OUT':
          return {
            ...prevState,
            isSignout: true,
            userToken: null,
          };
      }
    },
    {
      isLoading: true,
      isSignout: false,
      userToken: null,
    }
  );

  useEffect(() => {
    async function fetchUser() {
      let userData;
      try {
        userData = await AsyncStorage.getItem('userData')
      } catch (e) {
      }
      dispatch({ type: 'RESTORE_TOKEN', token: userData });
    }
    setTimeout(fetchUser, 1000)
  }, [])

  const authContext = useMemo(
    () => ({
      signIn: async data => {
        // In a production app, we need to send some data (usually username, password) to server and get a token
        // We will also need to handle errors if sign in failed
        // After getting token, we need to persist the token using `AsyncStorage`
        // In the example, we'll use a dummy token
        //TODO: API: sign in

        AsyncStorage.setItem('userData', data)

        dispatch({ type: 'SIGN_IN', token: data });
      },
      signOut: () => dispatch({ type: 'SIGN_OUT' }),
      signUp: async data => {
        // In a production app, we need to send user data to server and get a token
        // We will also need to handle errors if sign up failed
        // After getting token, we need to persist the token using `AsyncStorage`
        // In the example, we'll use a dummy token
        //TODO: API: sign up
        AsyncStorage.setItem('userData', data)

        dispatch({ type: 'SIGN_IN', token: 'dummy-auth-token' });
      },
    }),
    []
  );

  if (state.isLoading) {
    // We haven't finished checking for the token yet
    return <SplashScreen />
  }
  return (
    <AppContext.Provider value={authContext}>
      <NavigationContainer>
        {state.userToken ?
          <Stack.Navigator>
            <Stack.Screen name="Home" component={StoreMapView} />
            <Stack.Screen name="Store List" component={StoreListView} />
            <Stack.Screen name="Store Detail" component={StoreDetail} />
            <Stack.Screen name="Place Order" component={PlaceOrder} />

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

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
