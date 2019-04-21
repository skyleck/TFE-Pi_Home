using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace pi_home_mobileApp.ViewModel.UserViewModel
{
    public class LoginViewModel : BaseViewModel
    {
        private string _nickname;
        public string Nickname
        {
            get => _nickname;
            set
            {
                if (_nickname == value)
                    return;

                _nickname = value;

                OnPropertyChanged();
            }
        }

        private string _password;
        public string Password
        {
            get => _password;
            set
            {
                if (_password == value)
                    return;

                _password = value;

                OnPropertyChanged();
            }
        }

        public Command LoginCommandEvent { get; set; }
        private async Task LoginEvent()
        {
            var uri = new Uri("http://" + "192.168.1.11" + ":" + "5001" + "/api/users");
            d
            var response = await _client.GetAsync(uri);
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                var value = JsonConvert.DeserializeObject(content);
            }
        }

        public LoginViewModel() : base(title:"Login")
        {
            Nickname = "Nickname";
            Password = "Password";
            LoginCommandEvent = new Command(async () => await LoginEvent());
        }
    }
}