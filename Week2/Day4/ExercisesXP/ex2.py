'''
🌟 Exercise 2: Working with JSON
Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file.

'''

import json
import os
import sys


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parse the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Add a new key "birth_date" at the same level as the "name" key
data["company"]["employee"]["birth_date"] = "1990-01-01"

# To save in the same place with ex2.py
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
output_path = os.path.join(script_dir, 'employee_data.json')

# Step 5: Save the updated dictionary to a JSON file in the script's directory
with open(output_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Updated JSON data saved to '{output_path}'.")