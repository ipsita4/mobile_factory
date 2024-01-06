# Mobile Factory API

This project is a simple Flask application for a Mobile Factory Ordering System. The system allows users to place orders for smartphone components, and it validates the orders based on predefined rules. The application calculates the total price of the selected components and provides relevant information about the order.

## Installation

1. Create a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install Flask
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Create an order:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"components": ["I","A","D","F","K"]}' http://127.0.0.1:5000/orders
    ```

## API Endpoints

- `POST /orders`: Create a new order with a JSON payload containing the selected components.

## Component Codes

- **Screen**: A, B, C
- **Camera**: D, E
- **Port**: F, G, H
- **OS**: I, J
- **Body**: K, L

- ## Testing

To run the provided unit tests:

```bash
python test_app.py
```

# Response Codes

- **201:** Successful order creation.
- **400:** Invalid order components or structure.
- **500:** Internal server error.

## Examples

### Valid Order

**Request:**

```json
{ "components": ["I","A","D","F","K"] }
```

**Response:**
```json
{
    "order_id": "some-id",
    "parts": [
        "Android OS",
        "LED Screen",
        "Wide-Angle Camera",
        "USB-C Port",
        "Metallic Body"
    ],
    "total": 142.3
}

```
