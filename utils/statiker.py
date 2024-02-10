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
    if not "https://" in current:
        for j in ["src="]:
            if current.__contains__(j):
                # src="{% static 'userApp/' %}"

                # src="{% static 'userApp/
                # ' %}"

                tokens = current.split(j)
                part1 = tokens[0]
                part1 += j + "\"{% static \'userApp/"

                part2 = tokens[1]
                src = part2.split("\"")[1]

                part2 = part2.split(f"\"{src}\"")[1]

                part1 += src
                part1 += "' %}\""
                part1 += part2

                current =  part1

                break


    result.append(current)


with open("result.html", "w") as f:
    f.writelines(result)
    f.close()





