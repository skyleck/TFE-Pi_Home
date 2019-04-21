using MySql.Data.MySqlClient;
using pi_home_webAPI.Models;
using System;
using System.Collections.Generic;

namespace pi_home_webAPI.Components.Users
{
    public class UserDao
    {
        private MySqlConnection mySqlConnection;
       
        public User RunQuery(string query)
        {
            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            MySqlDataReader dataReader = cmd.ExecuteReader();

            User user = null;
            
            while (dataReader.Read())
            {
                user = new User(int.Parse(dataReader["id"].ToString()),
                                dataReader["login"].ToString(),
                                dataReader["firstname"].ToString(),
                                dataReader["lastname"].ToString(),
                                dataReader["password"].ToString());
            }

            mySqlConnection.Close();

            return user;
        }

        public User GetUser(int id)
        {
            string query = "SELECT * FROM user WHERE id=" + id;

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            MySqlDataReader dataReader = cmd.ExecuteReader();

            User user = null;
            
            while (dataReader.Read())
            {
                user = new User(int.Parse(dataReader["id"].ToString()),
                                dataReader["login"].ToString(),
                                dataReader["firstname"].ToString(),
                                dataReader["lastname"].ToString(),
                                dataReader["password"].ToString());
            }

            mySqlConnection.Close();

            return user;
        }

        public User GetLogin(string login, string password)
        {
            string query = "SELECT * FROM user WHERE login='" + login + "' AND password='" + password + "'";

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            MySqlDataReader dataReader = cmd.ExecuteReader();

            User userGet = null;

            while (dataReader.Read())
            {
                userGet = new User(int.Parse(dataReader["id"].ToString()),
                                dataReader["login"].ToString(),
                                dataReader["firstname"].ToString(),
                                dataReader["lastname"].ToString(),
                                dataReader["password"].ToString());
            }

            mySqlConnection.Close();

            return userGet;
        }
        
        public User GetUser(User user)
        {
            string query = "SELECT * FROM user";

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            MySqlDataReader dataReader = cmd.ExecuteReader();

            User userGet = null;

            while (dataReader.Read())
            {
                userGet = new User(int.Parse(dataReader["id"].ToString()),
                                dataReader["login"].ToString(),
                                dataReader["firstname"].ToString(),
                                dataReader["lastname"].ToString(),
                                dataReader["password"].ToString());
            }

            mySqlConnection.Close();

            return userGet;

        }

        public User GetUserByLogin(string login)
        {
            string query = "SELECT * FROM user WHERE login='" + login + "'";

            return RunQuery(query);
        }

        public User GetUserByFirstname(string firstname)
        {
            string query = "SELECT * FROM user WHERE firstname='" + firstname + "'";

            return RunQuery(query);
        }

        public User GetUserByLastname(string lastname)
        {
            string query = "SELECT * FROM user WHERE lastname='" + lastname + "'";

            return RunQuery(query);
        }

        public User GetUserByName(string firstname, string lastname)
        {
            string query = "SELECT * FROM user WHERE firstname='"+firstname+" AND lastname='" + lastname + "'";

            return RunQuery(query);
        }

        public List<User> GetAllUsers()
        {
            string query = "SELECT * FROM user";

            List<User> users = new List<User>();

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            MySqlDataReader dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                User user = new User(int.Parse(dataReader["id"].ToString()),
                                dataReader["login"].ToString(),
                                dataReader["firstname"].ToString(),
                                dataReader["lastname"].ToString(),
                                dataReader["password"].ToString());

                users.Add(user);
            }

            mySqlConnection.Close();

            return users;
        }

        public void AddUser(User user )
        {
            string query = "INSERT INTO user (login,firstname,lastname,password) VALUES ('"
                           + user.Login + "','" + user.Firstname + "','" + user.Lastname + "','" + user.Password + "')";

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            cmd.ExecuteNonQuery();

            mySqlConnection.Close();
        }

        public void UpdateUser(User user, int id)
        {
            string query = "UPDATE user SET " + "login='" + user.Login + "',firstname='" + user.Firstname
                    + "',lastname='" + user.Lastname + "',password='" + user.Password + "' WHERE id = " + id;

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            cmd.ExecuteNonQuery();

            mySqlConnection.Close();
        }

        public void DeleteUser(int id)
        {
            string query = "DELETE FROM user WHERE id = " + id;

            mySqlConnection.Open();

            MySqlCommand cmd = new MySqlCommand(query, mySqlConnection);
            cmd.ExecuteNonQuery();

            mySqlConnection.Close();
        }
        public UserDao(MySqlConnection mySqlConnection)
        {
            this.mySqlConnection = mySqlConnection;
        }
    }
}