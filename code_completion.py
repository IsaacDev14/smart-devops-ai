# AI-Suggested Code (e.g., GitHub Copilot)
# ----------------------------------------
# This code sorts a list of dictionaries by a given key using Python's built-in sorted() function.

data = [
    {"name": "Isaac", "age": 28},
    {"name": "John", "age": 22},
    {"name": "Mary", "age": 25}
]

# AI-suggested version
sorted_data_ai = sorted(data, key=lambda x: x["age"])
print("AI-Suggested Output:", sorted_data_ai)

# ----------------------------------------
# Manual Implementation (Written without AI Assistance)
# ----------------------------------------

def sort_dicts_by_key(data_list, sort_key):
    """Manually sorts a list of dictionaries by a given key using bubble sort."""
    n = len(data_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_list[j][sort_key] > data_list[j + 1][sort_key]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list

sorted_data_manual = sort_dicts_by_key(data.copy(), "age")
print("Manual Implementation Output:", sorted_data_manual)

# ----------------------------------------
# Comparison (in comments)
# The AI-generated version is more efficient (O(n log n)) using Python's optimized Timsort.
# The manual implementation (Bubble Sort) is O(n^2), slower on large datasets.
# AI helps reduce time and improve efficiency by suggesting the optimal method automatically.
