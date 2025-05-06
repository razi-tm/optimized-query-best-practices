# Optimized query - best practices

The API endpoint at `/api/order-item/`, managed by the `OrderItemViewSet`, has a satisfying performance after performing optimization and now has a response time under **200ms**.

## How to Run the Project

```bash
# Start the project
docker compose up -d

# Apply database migrations
docker compose exec fred python manage.py migrate

# Populate the database with sample data
docker compose exec fred python manage.py generate_data --users 20 --products 400 --orders 1000 --orderitems 4000

# The endpoint should now be accessible at http://localhost:8000/api/order-item/  
```
Note: Of course, you can run the project as you like (without Docker). Running by Docker is just for simplicity when running the project for the first time.

## Guide
Visit http://localhost:8000/silk/ for detailed performance analysis using **Silk**  
You also have a **Debug Toolbar** that appears on the right side of the browser  
And **QueryCount** through bash: sudo docker compose logs -f fred  

