import pandas

data = {'name' :["alice", "samuel", "dennis"],
            'age': [24, 34, 45],
            'city': ["kenya","uganda", "tanzania"]}

df = pandas.DataFrame(data)

with open("my_file.txt", "a") as file:
      file.write('df')
