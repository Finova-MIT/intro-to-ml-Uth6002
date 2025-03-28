import numpy as np
arr=np.array([[2,4,8],[55,45,76],[25,91,34]])
print(arr)

mean = np.mean(arr)
print(f"Mean is {mean}")
median = np.median(arr)
print(f"Median is {median}")
std = np.std(arr)
print(f"Std is {std}")
sum = np.sum(arr)
print(f"Total sum is {sum}")
reshaped = arr.reshape(9,1)
print(reshaped)