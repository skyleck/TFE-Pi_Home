using Microsoft.AspNetCore.Mvc;
using pi_home_webAPI.Components.Users;
using pi_home_webAPI.Models;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

namespace pi_home_webAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UsersController : ControllerBase
    {

        private UserComponent userComponentImpl;

        public UsersController(UserComponent userComponentImpl)
        {
            this.userComponentImpl = userComponentImpl;
        }

        [HttpGet]
        public IActionResult GetAllUser()
        {
            return Ok(userComponentImpl.GetAllUser());
        }

        [HttpGet("{id}")]
        public IActionResult GetUser(int id)
        {
            return Ok(userComponentImpl.GetUser(id));
        }

        [HttpPost]
        public IActionResult InsertUser(User user)
        {
            userComponentImpl.AddUser(user);
            return Ok("User added");
        }

        [HttpPut]
        public IActionResult UpdateUser(User user)
        {
            userComponentImpl.UpdateUser(user, user.Id);
            return Ok("User updated");
        }

        [HttpDelete]
        public IActionResult DeleteUser(int id)
        {
            userComponentImpl.DeleteUser(id);
            return Ok(id);
        }
    }
}