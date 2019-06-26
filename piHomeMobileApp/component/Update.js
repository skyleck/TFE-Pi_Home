import axios from 'axios';
import React, { Component } from 'react'
import { Alert, TouchableOpacity, Text, TextInput, View, StyleSheet } from 'react-native'
import AsyncStorage from '@react-native-community/async-storage'

export default class Registration extends Component {
    
    state = {
        user: this.props.navigation.state.params.user,
        lastname: this.props.navigation.state.params.user.lastname,
        firstname: this.props.navigation.state.params.user.firstname,
        password: "",
        confirmPassword: "",

        lastnameState: true,
        firstnameState: true,
        passwordState: true,
        confirmPasswordState: true,

        borderColor: '#000000',
        borderError: '#ff0000',

        token: ""
    }

    handleSubmit = async (event) => {

        this.setState({
            loginState: true,
            lastnameState: true,
            firstnameState: true,
            passwordState: true,
            confirmPasswordState: true
        })

        const user = {
            id: this.state.user.id,
            login: this.state.user.login,
            lastname: this.state.lastname,
            firstname: this.state.firstname,
            password: this.state.password,
            confirmPassword: this.state.confirmPassword,
            authorization: 0
        };

        const value = await AsyncStorage.getItem('token');
        this.setState({ token : value});
        const config = {
            headers: {
                'Content-Type': 'application/json;',
                'Authorization': 'Bearer ' + this.state.token
            }
        };

        axios.put("http://" + global.apiIp + "/api/user",user,config)
            .then(res => {
                this.props.navigation.navigate('ListUsers')
            })
            .catch((error) => {
                Alert.alert(JSON.stringify(error.response.data["msg"]))
                if(error.response.data["column"].length != 0){
                    for (let column of error.response.data["column"]){
                        this.setState({
                            [column+"State"]: false
                        })
                    }
                }
            })  
    }

    render(){
        return(
            <View style={styles.container}>
                <TextInput style={styles.inputs}
                    placeholder="Firstname"
                    underlineColorAndroid='transparent'
                    name="firstname"
                    value={this.state.firstname}
                    onChangeText={(firstname => this.setState({firstname}))}
                    borderColor ={this.state.firstnameState ? this.state.borderColor : this.state.borderError}
                />   
                <TextInput style={styles.inputs}
                    placeholder="Lastname"
                    underlineColorAndroid='transparent'
                    name="lastname"
                    value={this.state.lastname}
                    onChangeText={(lastname => this.setState({lastname}))}
                    borderColor ={this.state.lastnameState ? this.state.borderColor : this.state.borderError}
                />   
                <TextInput style={styles.inputs}
                    placeholder="Password"
                    underlineColorAndroid='transparent'
                    name="password"
                    secureTextEntry={true}
                    onChangeText={(password=> this.setState({password}))}
                    borderColor ={this.state.passwordState ? this.state.borderColor : this.state.borderError}
                />   
                <TextInput style={styles.inputs}
                    placeholder="Confirm Password"
                    underlineColorAndroid='transparent'
                    name="confirmPassword"
                    secureTextEntry={true}
                    onChangeText={(confirmPassword => this.setState({confirmPassword}))}
                    borderColor ={this.state.confirmPasswordState ? this.state.borderColor : this.state.borderError}
                />
                <TouchableOpacity style = {styles.button} onPress={this.handleSubmit}>
                    <Text style = {styles.textButton}>
                        Sign Up
                    </Text>
                </TouchableOpacity>                
            </View>
        );
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