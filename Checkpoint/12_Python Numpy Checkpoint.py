import numpy as np

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print("Grades:", grades)

# Calculate mean, median, and standard deviation
print("Mean:", np.mean(grades))
print("Median:", np.median(grades))
print("Standard Deviation:", np.std(grades))

# Find maximum and minimum grades
print("Maximum Grade:", np.max(grades))
print("Minimum Grade:", np.min(grades))

# Sort grades in ascending order
print("Sorted Grades:", np.sort(grades))

# Find index of highest grade
print("Index of Highest Grade:", np.argmax(grades))

# Count number of students who scored above 90
print("Number of Students Who Scored Above 90:", np.sum(grades > 90))

# Calculate percentage of students who scored above 90
print("Percentage of Students Who Scored Above 90:", np.mean(grades > 90) * 100)

# Calculate percentage of students who scored below 75
print("Percentage of Students Who Scored Below 75:", np.mean(grades < 75) * 100)

# Extract grades above 90 and put them in new array
high_performers = grades[grades > 90]
print("High Performers:", high_performers)

# Create new array of passing grades (above 75)
passing_grades = grades[grades > 75]
print("Passing Grades:", passing_grades)