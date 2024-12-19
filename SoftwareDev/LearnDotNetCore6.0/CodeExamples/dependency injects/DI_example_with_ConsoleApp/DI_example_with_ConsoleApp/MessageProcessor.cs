using DI_example_with_ConsoleApp;

public class MessageProcessor
{
    private readonly IMessageService _messageService;

    public MessageProcessor(IMessageService messageService)
    {
        _messageService = messageService;
    }

    public void Process(string message)
    {
        _messageService.SendMessage(message);
    }
}
