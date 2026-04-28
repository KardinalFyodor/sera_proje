from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(**name**)

model = tf.keras.models.load_model("model.h5")

@app.route("/predict", methods=["POST"])
def predict():
data = request.json

```
values = np.array(data["values"]).reshape(1, -1)
prediction = model.predict(values)

return jsonify({
    "result": prediction.tolist()
})
```

app.run(host="0.0.0.0", port=10000)
