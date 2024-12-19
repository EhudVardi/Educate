using DI_example_with_ConsoleApp;
using Microsoft.Extensions.DependencyInjection;
using System;

namespace DIExampleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1. Configure the DI container
            var serviceProvider = new ServiceCollection()
                .AddTransient<IMessageService, EmailService>() // Registers SmsService for IMessageService
                //.AddTransient<IMessageService, SmsService>() // Uncomment to switch to SmsService
                .AddTransient<MessageProcessor>() // Registers MessageProcessor
                .BuildServiceProvider();

            // 2. Resolve the dependency
            var processor = serviceProvider.GetService<MessageProcessor>();

            // 3. Use the resolved service
            processor?.Process("Hello, Dependency Injection!");

            Console.ReadLine();
        }
    }
}
