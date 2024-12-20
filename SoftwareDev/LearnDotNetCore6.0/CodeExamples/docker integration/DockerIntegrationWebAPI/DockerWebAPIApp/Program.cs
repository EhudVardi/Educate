var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
//if (app.Environment.IsDevelopment()) //enable swagger in all execution cases, including under docker
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// Disable HTTPS redirection in Docker (when running in the container)
// You can check if it's running in Docker or another environment to skip HTTPS redirection.
if (!app.Environment.IsDevelopment() && Environment.GetEnvironmentVariable("DOTNET_RUNNING_IN_CONTAINER") == "true")
{
    Console.WriteLine("Running inside Docker - skipping HTTPS redirection");
}
else
{
    app.UseHttpsRedirection();
}

app.UseAuthorization();

app.MapControllers();

app.Run();
