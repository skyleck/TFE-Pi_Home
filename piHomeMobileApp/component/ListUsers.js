import axios from 'axios';
import querystring from 'querystring'
import React, { Component } from 'react'
import { Alert, FlatList, SectionList, StyleSheet, Text,View } from 'react-native'
import AsyncStorage from '@react-native-community/async-storage';
import { ListItem } from 'react-native-elements';
import HeaderNavigationBar from './HeaderNavigationBar'

export default class ListUsers extends Component {

    state = {
        token: "",
        users: []
    }

    getUser = async () => {
        try{
            const value = await AsyncStorage.getItem('token');
            this.setState({ token : value});
            const config = {
                headers: {
                    'Content-Type': 'application/json;',
                    'Authorization': 'Bearer ' + this.state.token
                }
            };
    
            axios.get('http://'+global.apiIp+'/api/user',config)
                .then(res =>{
                        let users = res.data;
                        this.setState({users: users});
                    })
                .catch((error) => {
                    this.props.navigation.navigate('Home')
                });
        } catch(error){

        }
    };

    componentDidMount = () => {
        const { navigation } = this.props;
        this.focusListener = navigation.addListener("didFocus", () => {
            this.getUser();
        });
    };

    renderSeparator = () => {
        return (
          <View
            style={{
              height: 1,
              backgroundColor: '#CED0CE',
            }}
          />
        );
      };

    renderRow = ({item}) => (
        <ListItem
            title={item.login}
            subtitle={item.lastname + " " + item.firstname } 
            onPress={() => {this.props.navigation.navigate('UserPage',{user: item});}}
        />
    )

    render(){
        return(
            <View style={{ flex: 1 }}>
                <HeaderNavigationBar {...this.props} />
                <FlatList
                    data={this.state.users}
                    renderItem={this.renderRow}
                    keyExtractor={item => item.login}
                    ItemSeparatorComponent={this.renderSeparator}
                />
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
     flex: 1,
     paddingTop: 22
    },
    sectionHeader: {
      paddingTop: 2,
      paddingLeft: 10,
      paddingRight: 10,
      paddingBottom: 2,
      fontSize: 14,
      fontWeight: 'bold',
      backgroundColor: 'rgba(247,247,247,1.0)',
    },
    item: {
      padding: 10,
      fontSize: 18,
      height: 44,
    },
  })