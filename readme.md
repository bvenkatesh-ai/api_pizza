# Pizza Ordering System API

It allows users to fetch pizza menu items and place orders.

## Features

- Fetch pizza details by name
- Price calculation for order


## API Endpoints

### GET /menu

Fetch details of a specific pizza by name.

**Query Parameters:**
- `name` (string, required): The name of the pizza

**Example Request:**
```
GET /menu?name=Margherita
```

**Example Response:**
```json
{
  "id": 1,
  "name": "Margherita",
  "size": "Medium",
  "price": 8.99,
  "toppings": ["tomato sauce", "mozzarella", "basil"]
}
```

### POST /order

Place an order for multiple pizzas.

**Request Body:**
```json
{
  "items": [
    {
      "id": 1,
      "quantity": 2
    },
    {
      "id": 3,
      "quantity": 1
    }
  ]
}
```

**Example Response:**
```json
{
  "order_id": "12345678",
  "price": 28.97
}
```

## Error Handling

The API will return appropriate error messages with corresponding HTTP status codes if:
- A requested pizza is not found
- An invalid pizza ID is provided in the order

## Testing

You can use tools like curl, Postman, or any HTTP client to test the API endpoints.

Example using curl:

1. Fetch pizza details:
   ```
   curl "http://localhost:8000/menu?name=Margherita"
   ```

2. Place an order:
   ```
   curl -X POST "http://localhost:8000/order" \
        -H "Content-Type: application/json" \
        -d '{"items": [{"id": 1, "quantity": 2}, {"id": 3, "quantity": 1}]}'
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
