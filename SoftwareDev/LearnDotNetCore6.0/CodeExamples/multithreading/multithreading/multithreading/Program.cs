
//EXAMPLE - Tasks and async/await

//using System;
//using System.IO;
//using System.Threading.Tasks;

//class Program
//{
//    static async Task Main(string[] args)
//    {
//        string filePath = "example.txt";

//        Console.WriteLine("Starting file read...");
//        string content = await ReadFileAsync(filePath);
//        Console.WriteLine($"File Content: {content}");
//    }

//    static async Task<string> ReadFileAsync(string path)
//    {
//        using var reader = new StreamReader(path);
//        return await reader.ReadToEndAsync();
//    }
//}


//EXAMPLE - Parallel Class

//using System;
//using System.Threading.Tasks;

//class Program
//{
//    static void Main(string[] args)
//    {
//        Console.WriteLine("Starting parallel processing...");
//        Parallel.For(0, 10, i =>
//        {
//            Console.WriteLine($"Processing item {i} on thread {Task.CurrentId}");
//        });
//    }
//}





//EXAMPLE - IAsyncEnumerable

//using System;
//using System.Collections.Generic;
//using System.Threading.Tasks;

//class Program
//{
//    static async Task Main(string[] args)
//    {
//        await foreach (var number in GetNumbersAsync())
//            {
//            Console.WriteLine($"Received: {number}");
//        }
//    }

//    static async IAsyncEnumerable<int> GetNumbersAsync()
//    {
//        for (int i = 0; i < 10; i++)
//        {
//            await Task.Delay(2000); // Simulate work
//            yield return i;
//        }
//    }
//}



//EXAMPLE - Channels

//using System;
//using System.Threading.Channels;
//using System.Threading.Tasks;

//class Program
//{
//    static async Task Main(string[] args)
//    {
//        var channel = Channel.CreateUnbounded<int>();

//        var producer = Task.Run(async () =>
//        {
//            for (int i = 0; i < 10; i++)
//            {
//                await channel.Writer.WriteAsync(i);
//                Console.WriteLine($"Produced: {i}");
//                await Task.Delay(500);
//            }
//            channel.Writer.Complete();
//        });

//        var consumer = Task.Run(async () =>
//        {
//            await foreach (var item in channel.Reader.ReadAllAsync())
//            {
//                Console.WriteLine($"Consumed: {item}");
//            }
//        });

//        await Task.WhenAll(producer, consumer);
//    }
//}
