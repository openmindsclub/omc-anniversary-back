"""
DON'T CODE LIKE NPCs
USE STATIKER INSTEAD
"""

html = "/home/zak/Desktop/myDesk/djangoProjects/omc-anniversary-back/userApp/templates/userApp/index.html"

lines = []
result = []

with open(html, "r") as f:
    lines = f.readlines()
    f.close()

current = ""
for i in lines:
    current = i

    if current.__contains__("src="):
        # src="{% static 'userApp/' %}"

        # src="{% static 'userApp/
        # ' %}"
        pass
    
    result.append(current)
    


with open("result.html", "w") as f:
    f.writelines(result)
    f.close()
