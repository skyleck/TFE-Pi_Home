using MySql.Data.MySqlClient;
using pi_home_webAPI.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace pi_home_webAPI.Components.Users
{
    public class UserComponentImpl: UserComponent
    {
        private UserDao userDao;

        public UserComponentImpl(MySqlConnection mySqlConnection)
        {
            this.userDao = new UserDao(mySqlConnection);
        }

        public void AddUser(User user)
        {
            userDao.AddUser(user);
        }

        public void DeleteUser(int id)
        {
            userDao.DeleteUser(id);
        }

        public List<User> GetAllUser()
        {
            return userDao.GetAllUsers();
        }

        public User GetUser(int id)
        {
            return userDao.GetUser(id);
        }

        public User GetUser(User user)
        {
            return userDao.GetUser(user);
        }

        public User GetLogin(User user)
        {
            return userDao.GetLogin(user.Login, user.Password);
        }

        public User GetUserByLogin(string login)
        {
            return userDao.GetUserByLogin(login);
        }

        public User GetUserByFirstname(string firstname)
        {
            return userDao.GetUserByFirstname(firstname);
        }

        public User GetUserByLastname(string lastname)
        {
            return userDao.GetUserByLastname(lastname);
        }

        public User GetUserByName(string firstname, string lastname)
        {
            return userDao.GetUserByName(firstname, lastname);
        }

        public void UpdateUser(User user, int id)
        {
            userDao.UpdateUser(user, id);
        }
    }
}
