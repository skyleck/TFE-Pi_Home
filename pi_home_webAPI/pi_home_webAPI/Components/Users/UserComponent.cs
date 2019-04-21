using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using pi_home_webAPI.Models;

namespace pi_home_webAPI.Components.Users
{
    public interface UserComponent
    {
        User GetUser(int id);
        User GetUser(User user);
        User GetLogin(User user);
        User GetUserByLogin(string login);
        User GetUserByFirstname(string firstname);
        User GetUserByLastname(string lastname);
        User GetUserByName(string firstname, string lastname);
        List<User> GetAllUser();
        void AddUser(User user);
        void UpdateUser(User user, int id);
        void DeleteUser(int id);

    }
}
