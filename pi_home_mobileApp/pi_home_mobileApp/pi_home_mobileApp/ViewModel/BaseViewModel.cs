using System.ComponentModel;
using System.Net.Http;
using System.Runtime.CompilerServices;

namespace pi_home_mobileApp.ViewModel
{
    public class BaseViewModel : INotifyPropertyChanged
    {
        protected HttpClient _client;

        private string _title;

        public string Title
        {
            get => _title;
            set
            {
                if (_title == value)
                    return;
                _title = value;

                OnPropertyChanged();
            }
        }

        private bool _isBusy;
        public bool IsBusy
        {
            get => _isBusy;
            set
            {
                if (_isBusy == value)
                    return;

                _isBusy = value;

                OnPropertyChanged();
                OnPropertyChanged(nameof(IsNotBusy));
            }
        }
       
        private string _ip;
        public string IP
        {
            get => _ip;
            set
            {
                if (_ip == value)
                    return;
                _ip = value;

                OnPropertyChanged();
            }
        }

        private string _port;
        public string PORT
        {
            get => _port;
            set
            {
                if (_port == value)
                    return;
                _port = value;

                OnPropertyChanged();
            }
        }

        public bool IsNotBusy => !IsBusy;

        public event PropertyChangedEventHandler PropertyChanged;

        public BaseViewModel(string title)
        {
            Title = title;
            _client = new HttpClient();
            IP = "192.168.1.8";
            PORT = "3000";
        }

        public void OnPropertyChanged([CallerMemberName] string propertyName = "")
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
