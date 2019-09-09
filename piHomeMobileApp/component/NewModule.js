import axios from 'axios';
import querystring from 'querystring'
import React, { Component } from 'react'
import { Alert, FlatList, SectionList, StyleSheet, Text,View, TouchableOpacity} from 'react-native'
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

        axios.get('http://'+global.apiIp+'/api/moduleByName/None',config)
            .then(res =>{
                    let modules = res.data;
                    this.setState({modules: modules});
                })
            .catch((error) => {
                this.props.navigation.navigate('Home')
            });
    };

    handleSubmit = async (event) => {
        const value = await AsyncStorage.getItem('token');
        this.setState({ token : value});
        const config = {
            headers: {
                'Content-Type': 'application/json;',
                'Authorization': 'Bearer ' + this.state.token
            }
        };

        this.state.modules.map((module) => {
            axios.put('http://'+global.apiIp+'/api/module',module,config)
            .then(res => {
                modules = this.state.modules;
                modules.splice(this.findArrayPos(module.id),1);
                this.setState({modules:modules});
            })
            .catch((error) => {
                Alert.alert(JSON.stringify(error.response.data["msg"]))
            })  
        })
    }

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
            input={{
                value:item.name,
                onChangeText: (value) => {
                    modules = this.state.modules;
                    modules[this.findArrayPos(item.id)].name = value;
                    this.setState({modules:modules})
                }}}
            hideChevron
            title={item.ip}
        />   
    )

    renderFooter = () =>(
        <View style = {{alignItems: 'center' }} >
            <TouchableOpacity style = {styles.button} onPress={this.handleSubmit}>
                <Text style = {styles.textButton}>
                    Update
                </Text>
            </TouchableOpacity>
        </View>
    )

    render(){
        return(
            <View style={{ flex: 1 }}>
                <HeaderNavigationBar {...this.props} />
                <FlatList
                    data={this.state.modules}
                    extraData={this.state}
                    renderItem={this.renderRow}
                    keyExtractor={item => item.id}
                    ItemSeparatorComponent={this.renderSeparator}
                    ListFooterComponent={this.renderFooter}
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