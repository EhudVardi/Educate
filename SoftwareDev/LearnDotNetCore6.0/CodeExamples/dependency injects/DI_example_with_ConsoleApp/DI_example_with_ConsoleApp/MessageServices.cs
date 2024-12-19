using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DI_example_with_ConsoleApp
{
    public interface IMessageService
    {
        void SendMessage(string message);
    }

    public class EmailService : IMessageService
    {
        public void SendMessage(string message)
        {
            Console.WriteLine($"Email sent: {message}");
        }
    }

    public class SmsService : IMessageService
    {
        public void SendMessage(string message)
        {
            Console.WriteLine($"SMS sent: {message}");
        }
    }
}
