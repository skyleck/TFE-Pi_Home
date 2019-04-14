using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace pi_home_webAPI.Models
{
    public class User
    {
        /**
        public int id { get; set; }
        public string login { get; set; }
        public string firstname { get; set; }
        public string lastname { get; set; }
        public string password { get; set; }
        */

        private int _id;
        private string _login;
        private string _firstname;
        private string _lastname;
        private string _password;

        public User(int id,string login, string firstname, string lastname, string password)
        {
            Id = id;
            Login = login;
            Firstname = firstname;
            Lastname = lastname;
            Password = password;
        }

        public int Id { get => _id; set => _id = value; }
        public string Login { get => _login; set => _login = value; }
        public string Firstname { get => _firstname; set => _firstname = value; }
        public string Lastname { get => _lastname; set => _lastname = value; }
        public string Password { get => _password; set => _password = value; }
    }
}
