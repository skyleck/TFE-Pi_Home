import Login from './component/Login'
import ListUsers from './component/ListUsers'
import Registration from './component/Registration'
import UserPage from './component/UserPage'
import Update from './component/Update'
import ListModules from './component/ListModules'
import NewModules from './component/NewModule'

import {
  createStackNavigator,
  createAppContainer,
  createDrawerNavigator
} from 'react-navigation';

const DrawerStack = createDrawerNavigator({
  Login: { screen: Login, navigationOptions: {
    drawerLabel: () => null
  }},
  //Modules: {screen: Modules},
  ListUsers: { screen: ListUsers, navigationOptions: {drawerLabel:"Users" }},
  MyProfil: { screen: UserPage, navigationOptions: {drawerLabel:"My profil" }},
  ListModules: {screen: ListModules, navigationOptions: {drawerLabel:"Modules" }},
  NewModules: {screen: NewModules, navigationOptions: {drawerLabel:"New Modules" }},
  Registration : { screen: Registration, navigationOptions: {
    drawerLabel: () => null
  }},
  UserPage : {screen: UserPage, navigationOptions: {
    drawerLabel: () => null
  }},
  Update: {screen: Update, navigationOptions: {
    drawerLabel: () => null
  }}}, {
    initialRouteName: 'Login',
    contentOptions: {
      activeTintColor: '#e91e63',
    },
  });

const DrawerNavigation = createStackNavigator({
  DrawerStack: { screen: DrawerStack }
}, {
  headerMode: 'float',
  navigationOptions: ({navigation}) => ({
    headerStyle: {backgroundColor: 'green'},
    title: 'Logged In to your app!',
    headerLeft: <Text onPress={() => navigation.navigate('DrawerOpen')}>Menu</Text>
  })
})

const AppNavigator = createStackNavigator({
  Home: { screen: Login },
  ListUsers: {  screen: ListUsers},
  Registration : { screen: Registration},
  UserPage : {screen: UserPage},
  Update: {screen: Update},
  Drawer: { screen: DrawerNavigation }
},{
  // Default config for all screens
  headerMode: 'none',
  title: 'Main',
  initialRouteName: 'Registration'
})


global.apiIp = "192.168.1.61:5001";
global.id = 0;

const App = createAppContainer(DrawerStack);

export default App;