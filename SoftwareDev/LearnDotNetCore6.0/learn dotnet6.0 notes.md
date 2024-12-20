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

- Globalization and Localization

- Entity Framework: EF 6 vs EF Core
  