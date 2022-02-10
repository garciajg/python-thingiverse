with open("requirements.txt") as req:
    content = req.read()
    requirements = content.split("\n")
    print(requirements)
