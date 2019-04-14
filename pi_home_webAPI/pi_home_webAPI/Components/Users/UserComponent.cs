﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using pi_home_webAPI.Models;

namespace pi_home_webAPI.Components.Users
{
    public interface UserComponent
    {
        User GetUser(int id);
        List<User> GetAllUser();
        void AddUser(User user);
        void UpdateUser(User user, int id);
        void DeleteUser(int id);
    }
}
