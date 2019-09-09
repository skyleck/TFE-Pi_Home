import axios from 'axios'
import React, { Component } from 'react'
import { Alert,Text, TouchableOpacity, View, StyleSheet} from 'react-native'
import AsyncStorage from '@react-native-community/async-storage';

export default class User extends Component {

    state = {
        user : "",
        token:""
    }

    delete = async (event) => {
        const value = await AsyncStorage.getItem('token');
        this.setState({ token : value});
        const config = {
            headers: {
                'Content-Type': 'application/json;',
                'Authorization': 'Bearer ' + this.state.token
            }
        };
        axios.delete('http://'+global.apiIp+'/api/user/'+this.state.user.id,config)            
        .then(res => {
            this.props.navigation.navigate('ListUsers')
        })
    }

    getProfil = async() => {
        const value = await AsyncStorage.getItem('token');
        this.setState({ token : value});
        const config = {
            headers: {
                'Content-Type': 'application/json;',
                'Authorization': 'Bearer ' + this.state.token
            }
        };
        axios.get('http://'+global.apiIp+'/api/user/'+global.id,config)
            .then(res =>{
                let user = res.data[0];
                this.setState({user: user});
            })
    }

    componentDidMount = () => {
        if (this.props.navigation.state.params){
            this.setState({user: this.props.navigation.state.params.user})
        } else {
            this.getProfil();
        }
    };

    render(){
        return(
            <View style={{ flex: 1 }}>
                <View style={styles.content}>
                    <Text style={styles.name}>{this.state.user.lastname + " " + this.state.user.firstname}</Text>
                    <View style={{flex: 1, flexDirection: 'row'}}>
                        <TouchableOpacity style = {styles.button} onPress={() => {this.props.navigation.navigate('Update',{user: this.state.user});}}>
                            <Text style = {styles.textButton}>
                                Update
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style = {styles.button} onPress={this.delete}>
                            <Text style = {styles.textButton}>
                                Delete
                            </Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    content:{
      padding:30,
      alignItems: 'center',
    },  
    name:{
        fontSize:22,
        color:"#000000",
        fontWeight:'600',
    },    
    button: {
        width: 100,
        height: 50,
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
    },
  });