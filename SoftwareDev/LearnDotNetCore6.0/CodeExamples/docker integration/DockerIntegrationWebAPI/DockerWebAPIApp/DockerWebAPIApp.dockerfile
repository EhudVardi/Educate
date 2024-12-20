# Use the official .NET 6 SDK image for building the application
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /app

# Copy project files and restore dependencies
COPY . .
RUN dotnet restore

# Publish the application in Release mode
RUN dotnet publish -c Release -o out

# Use the official ASP.NET Core runtime for the final image
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app

# Copy the published files into the runtime image
COPY --from=build /app/out .

# Expose port 80 for the application
EXPOSE 80

# Command to run the application
ENTRYPOINT ["dotnet", "DockerWebAPIApp.dll"]
