# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Price data
price_data = {
    "A": 10.28,
    "B": 24.07,
    "C": 33.30,
    "D": 25.94,
    "E": 32.39,
    "F": 18.77,
    "G": 15.13,
    "H": 20.00,
    "I": 42.31,
    "J": 45.00,
    "K": 45.00,
    "L": 30.00
}

# Part data
part_data = {
    "A": "LED Screen",
    "B": "OLED Screen",
    "C": "AMOLED Screen",
    "D": "Wide-Angle Camera",
    "E": "Ultra-Wide-Angle Camera",
    "F": "USB-C Port",
    "G": "Micro-USB Port",
    "H": "Lightning Port",
    "I": "Android OS",
    "J": "iOS OS",
    "K": "Metallic Body",
    "L": "Plastic Body"
}

def calculate_total(components):
    total = sum(price_data[component] for component in components)
    return round(total, 2)

def validate_order(components):
    # Required parts for each category
    required_categories = {
        "Screen": ["A", "B", "C"],
        "Camera": ["D", "E"],
        "Port": ["F", "G", "H"],
        "OS": ["I", "J"],
        "Body": ["K", "L"]
    }

    # Create sets to store selected parts for each category
    selected_categories = {category: set() for category in required_categories}

    # Iterate over the provided components
    for component in components:
        # Find the category to which the component belongs
        category = None
        for key, values in required_categories.items():
            if component in values:
                category = key
                break

        if category:
            selected_categories[category].add(component)
        else:
            # Invalid component found
            print(f"Invalid component code: {component}")
            return False

    # Check if each category has exactly one selected component
    for category, selected_set in selected_categories.items():
        if len(selected_set) != 1:
            print(f"Invalid number of components for {category}")
            return False

    # If all checks pass, the order is valid
    return True


@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        components = data.get('components', [])

        if validate_order(components):
            order_id = "some-id"  # You might generate a unique ID here
            total = calculate_total(components)
            parts = [part_data[component] for component in components]

            response_data = {
                "order_id": order_id,
                "total": total,
                "parts": parts
            }

            return jsonify(response_data), 201
        else:
            return jsonify({"error": "Invalid order components"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
