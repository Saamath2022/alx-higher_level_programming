
base_data = {"id": 1}
rectangle_data = {"width": 5, "height": 10, "x": 2, "y": 3}

import json

with open("base_data.json", "w") as f:
    json.dump(base_data, f)

with open("rectangle_data.json", "w") as f:
    json.dump(rectangle_data, f)
