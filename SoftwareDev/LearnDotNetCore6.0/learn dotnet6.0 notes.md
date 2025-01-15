# Notes while learning .Net Core (dotnet 6.0)

## Installation (under windows)
### Install Visual Studio Community
### Install .NET 6.0 SDK
- Open the Visual Studio Installer -> Modify -> Individual Components
- Visual Studio Installer typically Automatically installs SDK versions that align with the selected workloads and features
- Verify installation\
  run `dotnet --version`

## Learn modern dotnet (core / dotnet6.0)
### Examples that show the differences between legacy .net framework and .net core (.net)
#### publishing applications & Cross-Platform Capabilities
- publish to linux env
  - run this command on VS powershell window\
  `dotnet publish -c Release -r linux-x64 --self-contained`
  - published files will be generated in
  `bin/Release/net6.0/linux-x64/publish`
  - copy the entire folder to a linux system and dir into it.
  - verify that the main file named after the app name is allowed to run `ls -l [APP_NAME]`\
  add exec permissions if not enabled `chmod +x [APP_NAME]`
  - exec the app `./[APP_NAME]`

- File I/O Application: New APIs in .NET
  - Simpler syntax and async/await support in .NET 6\
  - Also, there's performance improvements in file handling
  example:
  ```
  await File.WriteAllTextAsync("example.txt", "Hello .NET!");
  var content = await File.ReadAllTextAsync("example.txt");
  ```

- Web API: ASP.NET vs ASP.NET Core
  - Create a new project - ASP.NET Core Web API - auto generated "WeatherForecast" controller
  - Add a Custom API Endpoint - create a new model (data struct) and a controller to expose it.
  - Run and make requests - use built-in Swagger for testing, make requests to the api using apps like postman, or write c# client to make requests.

- Dependency Injection Example
  - create a simple console app harnessing DI
    - Install the Microsoft.Extensions.DependencyInjection package using nuget
    - define the interface and its implementation varients
    - define a processor class to which the injection will occur
    - on main, 
      - create a ServiceCollection which is the service provider
      - call AddTransient on it to add a provider (this is where the injection is configured), call AddTransient to add a processor instance, then call BuildServiceProvider to build the service
      - then get the processor instance from the provider and call its process func. getting it will incure the injection of the specified interface implementation and the processor will then use it.

- Desktop Application: WinForms/WPF Modernization
  - Benefits of .NET Core/6/7/8 for Desktop Apps - Performance Improvements, Modern APIs and Libraries and Future Support
  - Key Changes in WinForms and WPF on .NET Core
    - High DPI Improvements
    - Updated Controls for WinForms/WPF controls for efficiency and look
    - Dependency Injection Support
    - Single File Deployment: Bundle the entire application and runtime into a single executable
    - App Trimming: Reduce application size by trimming unused parts of the runtime and libraries.
    - New Rendering Engine for WPF: Improved rendering pipeline for better performance

- Multithreading and Asynchronous Programming
  - Tasks and async/await - 
    - Fully asynchronous APIs for file operations (ReadToEndAsync), where in .net framework we use BeginRead/EndRead
  - Parallel Class - a class that allows to put computations into parallel threads in a for loop manner.
    - Improved performance and thread management
  - IAsyncEnumerable - Modern asynchronous allows asynchronous iteration over collections to process data streams lazily
    - a foreach loop interated data source can be specified, and the loop will wait for items to be received.
  - Channels - a modern way to implement producer-consumer patterns
    - Channels simplify asynchronous producer-consumer scenarios as opposed to .net framework where a  custom implementations is required or complex use of BlockingCollection

- Cross-Platform Deployment: Docker
  - integration with Docker, allowing for execution in a platform independent manner, by adding a dockerfile in the root of the project
    - built example webapi app - default weather api app, disabled ssl (https) access for simplicity, enabled swagger in all cases (even if running in a container and not in dev env)
    - use docker to build a docker file\
      `docker build -f [DOCKERFILE_FILENAME] - t [DOCKER_OUTPUT_IMAGE_FILENAME] [PATH_TO_DOTNET_PROJECT]`\
      in our example:\
      `docker build -f DockerWebAPIApp.dockerfile -t dockerwebapiapp .`
    - create a container and run it, exposing a url to access it.\
      `docker run -d -p [HOST_PORT]:[CONTAINER_PORT] [DOCKER_IMAGE]`\
      ("-d" means detached (no console attached), "-p" map host port to container port, the image should already be available on docker desktop)\
      in our example:\
      `docker run -d -p 8080:80 -p 8081:443 dockerwebapiapp`
    - now the container should run. now we can navigate to:\
      WeatherForecast api controller - `http://localhost:8080/WeatherForecast`\
      swagger dev gui - `http://localhost:8080/swagger`

- Modern Language Features
  - Global Using Directives\
    use a single code file that contains using statments that apply to all code files
  
  - File-Scoped Namespaces\
    allowing to state a namespace that contains the entire code in a file, without the braces.\
    instead of `namespace NS { ...code here... }` we can do `namespace NS; ...code here...`
  
  - Top-Level Statements - \
    remove the need for boilerplate main function. the main file IS the main function content
  
  - Record Structs\
    A <b>record</b> is a reference type with built-in functionality for immutability, value equality, and simple syntax for data classes.\
    A <b>struct</b> is a value type optimized for scenarios where performance and memory footprint are crucial.\
    <b>Record Structs</b> combine these concepts, enabling you to create immutable, value-type data structures with minimal syntax and automatic value equality support.\
    Features:
    - Value Type - stored in the stack like structs.
    - Immutability - immutable, properties cannot be changed after initialization
    - Value-Based Equality - built in ability for two instances to be compared for equality
    - Concise Syntax
    - Positional Record Structs - can be declared with positional parameters.
    - No Default Constructor - no parameterless ctor, similar to structs
    - Cannot Derive - sealed and cannot be inherited
    - Boxing - boxing occurs when casting to object, affects perf'
    - Nullable Properties - carefull defining of properties that can hold null to avoid runtime issues
    ```
    public readonly record struct Point(int X, int Y);
    var point1 = new Point(3, 4);
    var point2 = new Point(3, 4);
    Console.WriteLine(point1 == point2); // True (Value-based equality)
    Console.WriteLine(point1); // Outputs: Point { X = 3, Y = 4 }
    // point1.X = 5; // Immutability example (uncommenting will cause a compile-time error)
    ```
    
  - Extended Property Patterns - \
    advanced pattern matching with nested properties
  
  - Global Constants in Interpolated Strings - interpolated strings ("${VAR_NAME}" syntax) are allowed to be defined as constant\
    ```
    const string AppName = "MyApp";
    const string Version = "1.0";
    const string FullInfo = $"{AppName} - Version {Version}";
    ```
    
  - Lambda Improvements\
    1. Natural Type for Lambdas - inferred natural type if the compiler can determined it\
       ```
       Func<int, int, int> add = (a, b) => a + b; // old, explicitly defined as "Func<int,int,int>"
       var add = (int a, int b) => a + b; // new, compiler auto' determines it as "Func<int,int,int>"
       ```
    2. Lambda Return Types - explicitly define the return type of a lambda exp'
       ```
       var greet = string (string name) => $"Hello, {name}!";
       ```
    3. Attributes on Lambdas - can attach attributes to a lambda exp'
    4. Improved Delegates - can now assign a lambda to a specific delegate type without manual casting
       ```
       delegate int Operation(int a, int b);
       Operation multiply = (a, b) => a * b;
       ```
    5. Use with Anonymous Types - lambda works naturally with an anonymous type
       ```
       var printer = (object obj) => Console.WriteLine(obj.ToString());
       printer(new { Name = "John", Age = 30 });
       ```
    6. Target-Type Inference - lambdas can be target-typed more effectively\
       The compiler can infer the type of the lambda based on the expected type, such as a delegate or a generic parameter
       ```
       void Process(Func<int, int> operation) {
           Console.WriteLine(operation(5));
       }
       Process(x => x * 2); // No need to specify types in the lambda
       ```
    7. Scoped Lambda Variables - variables declared in lambdas are scoped only to the lambda itself.
    
  - Interpolated String Handlers - \
    Improves performance of string interpolation, especially in libraries
  
  - Null Parameter Checking - Simplifies null checks for method arguments with the `!!` operator\
    in this example `void PrintMessage(string message!!) { ...func code...}` the func will automaticall throw ArgumentNullException is message is null
  
  - Async Streams Enhancements - Improved support for asynchronous data streams (IAsyncEnumerable)\
    Using the async,await and yield operators
    ```
    await foreach (var item in FetchDataAsync()) { 
        Console.WriteLine(item); 
    }
    async IAsyncEnumerable<int> FetchDataAsync() {
        for (int i = 0; i < 5; i++) {
            yield return i;
            await Task.Delay(500);
        }
    }
    ```
  
  - Improved with Expression for Anonymous Types - \
    Allows cloning and modifying anonymous types with the "with" operator\
    ```
    var person = new { Name = "John", Age = 30 };
    var olderPerson = person with { Age = 35 };
    Console.WriteLine(olderPerson); // -> { Name = John, Age = 35 }
    ```
  
  - CallerArgumentExpression Attribute\
    an attribute that can be applied to a method parameter. it automaticall captures the expression (as a string) that was used to pass an arg to a method at the call, and injects it to the method to be used.\
    It can be used in unit testing to make assertions, It allows to provide detailed error messages when validating arguments in a method and to capture and log the exact expressions passed to methods
    ```
    using System;
    using System.Runtime.CompilerServices;

    public static class ArgumentLogger {
        public static void LogArgument(
            object? argument,
            [CallerArgumentExpression("argument")] string? argumentExpression = null) {
            Console.WriteLine($"Argument: {argument}");
            Console.WriteLine($"Expression: {argumentExpression}");
        }
    }
    class Program {
        static void Main() {
            int x = 42;
            ArgumentLogger.LogArgument(x + 1);
        }
    }
    ```

  - Minimal APIs for Web Applications - Simplifies building small REST APIs with concise code.\
    Perfect for microservices or simple APIs
    ```
    var app = WebApplication.CreateBuilder(args).Build();
    app.MapGet("/", () => "Hello, World!");
    app.Run();
    ```
    
  - Support for Default Interface Methods - Interfaces can now have default implementations for methods\
    ```
    public interface IMyInterface
    {
        void DoWork() => Console.WriteLine("Default implementation");
    }
    ```

  - Improved Task Parallel Library (TPL)
    1. ThreadPool class optimized to handle tasks more efficiently by reducing contention and making better use of system resources
       ```
       Parallel.For(0, 10, i => {
           Console.WriteLine($"Processing {i} on Thread {Thread.CurrentThread.ManagedThreadId}");
       });
       ```
    2. Parallel.For and Parallel.ForEach Enhancements
       ```
       Parallel.ForEach(Enumerable.Range(1, 10), number => {
           Console.WriteLine($"Processing {number}");
       });
       ```
    3. ValueTask Enhancements - works seamlessly in more scenarios and improved perf'
       ```
       async ValueTask<int> PerformCalculationAsync() {
           await Task.Delay(100); // Simulate asynchronous work
           return 42;
       }
       var result = await PerformCalculationAsync();
       Console.WriteLine(result);
       ```
    4. Task.WaitAny and Task.WaitAll Improvements - better performance when dealing with multiple tasks
       ```
       var task1 = Task.Run(() => "Result from Task 1");
       var task2 = Task.Run(() => "Result from Task 2");
       var completedTask = await Task.WhenAny(task1, task2);
       Console.WriteLine(await completedTask); // Prints the result of the first completed task
       ```
    5. Task.Run and Task.Yield Improvements - updates to better balance work across threads
       ```
       await Task.Run(() => {
           Console.WriteLine("Running on a background thread");
       });

       ```
    6. Async Streams (IAsyncEnumerable) Integration - \
       full integration with TPL, allowing seamless iteration over asynchronous data sources
       ```
       async IAsyncEnumerable<int> GenerateNumbersAsync() {
           for (int i = 0; i < 5; i++) {
               await Task.Delay(500); // Simulate data fetching
               yield return i;
           }
       }
       await foreach (var number in GenerateNumbersAsync()) {
           Console.WriteLine($"Received: {number}");
       }

       ```
    7. Improved Cancellation Support - \
       Cancellation tokens are better integrated into TPL methods, ensuring graceful task termination.
       ```
       var cts = new CancellationTokenSource();
       Task.Run(async () => {
           for (int i = 0; i < 10; i++) {
               if (cts.Token.IsCancellationRequested) {
                   Console.WriteLine("Task was cancelled!");
                   return;
               }
               Console.WriteLine($"Processing {i}");
               await Task.Delay(500); // Simulate work
           }
       }, cts.Token);
       
       // Cancel the task after 2 seconds
       await Task.Delay(2000);
       cts.Cancel();
       ```
    8. Improved PLINQ (Parallel LINQ) - \
       PLINQ is faster and more efficient, especially with modern multi-core CPUs\
       ```
       var numbers = Enumerable.Range(1, 1000000);
       var evenNumbers = numbers.AsParallel()
                                .Where(n => n % 2 == 0)
                                .ToList();
       Console.WriteLine($"Found {evenNumbers.Count} even numbers");
       ```
    9.  Better Diagnostic Tools - \
       Improved logging and diagnostic capabilities for monitoring task execution and debugging performance issues.\
       Use dotnet-trace or dotnet-counters to monitor task behavior\
       `dotnet-counters monitor System.Threading`


- Globalization and Localization

- Entity Framework: EF 6 vs EF Core
  