using Microsoft.AspNetCore.Mvc;
using pi_home_webAPI.Components.Users;
using pi_home_webAPI.Models;

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
        public IActionResult GetUser(User user)
        {
            return Ok(userComponentImpl.GetUser(user));
        }

        [HttpGet("{id}")]
        public IActionResult GetUser(int id)
        {
            return Ok(userComponentImpl.GetUser(id));
        }

        [HttpGet("[action]")]
        public IActionResult Login(User user)
        {
            return Ok(userComponentImpl.GetLogin(user));
        }

        [HttpGet("[action]")]
        public IActionResult GetUserByLogin(User user)
        {
            return Ok(userComponentImpl.GetUserByLogin(user.Login));
        }

        [HttpGet("[action]")]
        public IActionResult GetUserByFirstname(User user)
        {
            return Ok(userComponentImpl.GetUserByFirstname(user.Firstname));
        }

        [HttpGet("[action]")]
        public IActionResult GetUserByLastname(User user)
        {
            return Ok(userComponentImpl.GetUserByLastname(user.Lastname));
        }

        [HttpGet("[action]")]
        public IActionResult GetUserByName(User user)
        {
            return Ok(userComponentImpl.GetUserByName(user.Firstname, user.Lastname));
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
            return Ok("User deleted");
        }
    }
}