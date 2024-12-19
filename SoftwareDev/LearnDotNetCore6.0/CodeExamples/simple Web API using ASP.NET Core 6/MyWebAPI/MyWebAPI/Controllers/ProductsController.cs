using Microsoft.AspNetCore.Mvc;
using MyWebAPI.Models;

namespace MyWebAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private static List<Product> Products = new()
    {
        new Product { Id = 1, Name = "Laptop", Price = 1000.00m },
        new Product { Id = 2, Name = "Phone", Price = 500.00m }
    };

    [HttpGet]
    public ActionResult<IEnumerable<Product>> GetProducts()
    {
        return Ok(Products);
    }

    [HttpGet("{id}")]
    public ActionResult<Product> GetProduct(int id)
    {
        var product = Products.FirstOrDefault(p => p.Id == id);
        if (product == null)
            return NotFound();

        return Ok(product);
    }

    [HttpPost]
    public ActionResult AddProduct(Product product)
    {
        product.Id = Products.Any() ? Products.Max(p => p.Id) + 1 : 1;
        Products.Add(product);
        return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
    }

    [HttpDelete("{id}")]
    public ActionResult DeleteProduct(int id)
    {
        var product = Products.FirstOrDefault(p => p.Id == id);
        if (product == null)
            return NotFound();  

        Products.Remove(product);
        return NoContent();
    }
}
