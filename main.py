import numpy as np

user_input = input("Please enter 9 numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    }

    return calculations



try:
    result = calculate(numbers)
    print(result)
except ValueError as e:
    print(e)
