# Dictionaries
# contains key-value pairs (key -> value)
# syntax: {"key1": value1, "key2": value2}
student_1 = {
    # 'key': value
    'name': 'Benedek',
    'stream': 'DevOps',
    'completed_lessons': 4,
    'completed_lesson_names': ['lists', 'tuples', 'strings']
}
print(type(student_1))
print(student_1)  # print whole dictionary
print(student_1['stream'])  # print value with key [argument]
print(student_1['completed_lesson_names'])
print(student_1['completed_lesson_names'][0])
student_1['completed_lessons'] = 3  # reassignment/assignment
student_1['completed_lesson_names'].remove('strings')  # remove item from a list value

# Built-in Methods
print(student_1.keys())  # print all keys
print(student_1.values())  # print all values
