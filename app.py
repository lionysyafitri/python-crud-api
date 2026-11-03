from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database sederhana untuk contoh CRUD
items = []


@app.route("/health", methods=["GET"])
def health_check():
  return jsonify({"status": "healthy", "message": "API is running smoothly"}), 200


@app.route("/items", methods=["GET"])
def get_items():
  return jsonify(items), 200


@app.route("/items", methods=["POST"])
def create_item():
  data = request.get_json()
  if not data or "name" not in data:
    return jsonify({"error": "Invalid request, 'name' is required"}), 400

  new_item = {"id": len(items) + 1, "name": data["name"]}
  items.append(new_item)
  return jsonify(new_item), 201


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)