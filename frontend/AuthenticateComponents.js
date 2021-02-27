import React, { useState, useEffect } from 'react';
import {  View, TextInput, Text, TouchableOpacity} from 'react-native';
import AppContext from './AppContext';
import Toast from 'react-native-toast-message';
import styles from './styles';

const SignInScreen = (props) => {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    const { signIn } = React.useContext(AppContext);

    return (
        <View 
            style={styles.container}>

            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Username"
                    value={username}
                    onChangeText={setUsername}
                />
            </View>
            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Password"
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry
                />
            </View>
            <TouchableOpacity
                onPress={() => props.navigation.navigate('Sign Up')}>
                <Text style={styles.forgot_button}>No Account? Please Sign Up</Text>
            </TouchableOpacity>

            <TouchableOpacity 
            onPress={() => signIn({ username, password })}
            style={styles.loginBtn}>
                <Text style={styles.loginText}>LOGIN</Text>
            </TouchableOpacity>
        </View>
    );
}

const SignUpScreen = () => {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [phone, setPhone] = React.useState('');
    const [email, setEmail] = React.useState('');
    const [repeatpassword, setRepeatPassword] = React.useState('');

    const { signUp } = React.useContext(AppContext);

    return (
        <View
            style={styles.container}>
            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Username"
                    value={username}
                    onChangeText={setUsername}
                />
            </View>
            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Email"
                    value={email}
                    onChangeText={setEmail}
                />
            </View>
            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Phone"
                    value={phone}
                    onChangeText={setPhone}
                />
            </View>
            <View style={styles.inputView}>
                <TextInput
                    style={styles.TextInput}
                    placeholder="Password"
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry
                />
            </View>
            

            <TouchableOpacity
                onPress={() => signUp({ username, password, })}
                style={styles.loginBtn}>
                <Text style={styles.loginText}>SIGN UP</Text>
            </TouchableOpacity>

        </View>
    );
}


export {
    SignInScreen,
    SignUpScreen
}