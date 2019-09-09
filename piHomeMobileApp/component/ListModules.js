import axios from 'axios';
import querystring from 'querystring'
import React, { Component } from 'react'
import { Alert, FlatList, SectionList, StyleSheet, Text,View } from 'react-native'
import AsyncStorage from '@react-native-community/async-storage';
import { ListItem } from 'react-native-elements';
import HeaderNavigationBar from './HeaderNavigationBar'	
import { Switch} from 'react-native'

export default class ListModules extends Component {
    
    state = {
        token: "",
        modules: []
    }

    getModules = async () => {
        const value = await AsyncStorage.getItem('token');
        this.setState({ token : value});
        const config = {
            headers: {
                'Content-Type': 'application/json;',
                'Authorization': 'Bearer ' + this.state.token
            }
        };

        axios.get('http://'+global.apiIp+'/api/module',config)
            .then(res =>{
                    let modules = res.data;
                    this.setState({modules: modules});
                })
            .catch((error) => {
                this.props.navigation.navigate('Home')
            });
    };

    componentDidMount = () => {
        const { navigation } = this.props;
        this.focusListener = navigation.addListener("didFocus", () => {
            this.getModules();
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

    findArrayPos = (id) => {
        for(var i = 0; i < this.state.modules.length; i++) {
            if(this.state.modules[i]["id"] === id) {
                return i;
            }
        }
    }
    
    renderRow = ({item}) => (
        <ListItem
            switch={{
                value:this.state.modules[this.findArrayPos(item.id)].state === 1 ? true : false,
                onValueChange: async (value) => {
                    modules = this.state.modules;
                    for(var i = 0; i < modules.length; i++) {
                        if(modules[i]["id"] === item.id) {
                            modules[i]["state"] = value ? 1 : 0;
                            this.setState({modules: modules})
                        }
                    }
                    const token = await AsyncStorage.getItem('token');
                    this.setState({ token : token});
                    const config = {
                        headers: {
                            'Content-Type': 'application/json;',
                            'Authorization': 'Bearer ' + this.state.token
                        }
                    };

                    const module = {
                        id:item.id,
                        name:item.name,
                        ip:item.ip,
                        state:item.state,
                        action:"changeState"
                    }

                    axios.put("http://" + global.apiIp + "/api/module",module,config)
                        .catch((error) => {
                            this.props.navigation.navigate('Home')
                        })
                }
            }}
            hideChevron
            title={item.name}
            subtitle={item.ip}
        />   
    )

    render(){
        return(
            <View style={{ flex: 1 }}>
                <HeaderNavigationBar {...this.props} />
                <FlatList
                    data={this.state.modules}
                    extraData={this.state}
                    renderItem={this.renderRow}
                    keyExtractor={item => item.name}
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