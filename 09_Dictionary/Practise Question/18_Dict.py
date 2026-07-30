# Creating a Dictionary from the two list (most important)

Subject = ["English","Hindi","Math", "Physics","Chemistry"]
Scores = [88,76,98,91,77]

result = {s: sc for s, sc in zip(Subject,Scores)}
print(result)


# Most Simple want to combine the Two list into dictionary is:
res = dict(zip(Subject,Scores))
print(res)

# But when you want to combine them by modyfing or any other changes you should use:
# {s: sc for s, sc in zip(Subject,Scores)}

