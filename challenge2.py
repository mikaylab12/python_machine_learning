# challenge 2 : creating a histogram
import matplotlib.pyplot as plt
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
# placing x and y labels and their headings
plt.xlabel("nums")
plt.ylabel("bins")
# histogram heading
plt.title("Histogram of nums against bins")
# creating the histogram
plt.hist(nums,bins, color ='#5bb425')
plt.show()