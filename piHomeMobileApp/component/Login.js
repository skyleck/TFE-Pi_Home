import axios from 'axios';
import AsyncStorage from '@react-native-community/async-storage';
import React, { Component } from 'react'
import { Alert, TouchableOpacity, Text, TextInput, View, StyleSheet } from 'react-native'

export default class Login extends Component {

    state = {
        login: '',
        password: ''
    }

    _storeData = async (id) => {
        try{
            await AsyncStorage.setItem('id',id)
        }
        catch(error){
            
        }
    }

    handleSubmit = event => {
        const login = {
            id: 0,
            login: this.state.login,
            password: this.state.password
        };

        const config = {
            headers: {
                'Content-Type': 'application/json;',
            }
        };

        axios.post('http://'+global.apiIp+'/api/login',login,config)
              .then(res => {
                AsyncStorage.setItem('token',res.data["access_token"])
                global.id = res.data["id"];
                this.props.navigation.navigate('ListUsers')
              })
              .catch((error) => {
                  Alert.alert(error.response.data);
              });
    }

    signUp = event => {
        this.props.navigation.navigate('Registration')
    }

    render(){
        return(
            <View style={styles.container}>
                <TextInput style={styles.inputs}
                    placeholder="Login"
                    underlineColorAndroid='transparent'
                    name="login"
                    onChangeText={(login => this.setState({login}))}
                />
                <TextInput style={styles.inputs}
                    placeholder="Password"
                    secureTextEntry={true}
                    underlineColorAndroid='transparent'
                    name="password"
                    onChangeText={(password => this.setState({password}))}
                />
            <TouchableOpacity style = {styles.button} onPress={this.handleSubmit}>
                <Text style = {styles.textButton}>
                    Sign In
                </Text>
            </TouchableOpacity>
            <Text style={{color: 'blue', marginTop:10}} onPress={this.signUp}>Have not you an account ? Sign up here !</Text>
            </View> 
        )
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#DCDCDC',
    },
    inputs:{
        width:250,
        height:45,
        marginBottom:20,
        borderRadius:30,
        borderWidth: 0.5,
        borderColor: '#000000',
        backgroundColor: '#FFFFFF',
    },
    button: {
        width: 100,
        backgroundColor: '#2F99CE',
        borderColor: 'white',
        borderWidth: 1,
        borderRadius: 12,
        color: 'white',
        fontSize: 24,
        fontWeight: 'bold',
        overflow: 'hidden',
        padding: 12,
    },
    textButton:{
        color:'#ffffff',
        textAlign:'center',
    }
})

