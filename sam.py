class person:
    def __init__(self, name, age, height):
        self.jina = name
        self.miaka = age
        self.urefu = height

    def __str__(self):
        return f"hello {self.jina} , you are {self.miaka} years old, and  {self.urefu} metres. "
    def end(self):
        print("it was good interacting with you")
        return

p = person("samuel", 20, 1.56)
print(p)
p.end()