from flask import Flask, jsonify
import os
 
app = Flask(__name__)
 
@app.get("/ping")
def ping():
    return jsonify(ok=True, env=os.environ.get("ENV", "local"))
 
# Entrada opcional para desarrollo (no usada con Gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
