import csv

def save(playlist):
    with open('playList.csv','a', newline='') as file:
        writer = csv.writer(file)
        for obj in playlist:
            writer.writerow(str(obj).split(","))

def load():
    pass