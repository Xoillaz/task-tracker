from datetime import datetime
import json

class Issues:
    def add(detail):
        data = load()
        tid = len(data) + 1
        data.append(Task(detail, tid).to_dict())
        save(data)
        log("added", tid)

    def mv(tid, detail):
        data, i = load(), int(tid)-1
        data[i]['detail'] = detail
        save(data)
        log("updated", tid)

    def mk(tid, status):
        data, i = load(), int(tid)-1
        data[i]['status'] = status if status!="in-progress" else "-ing"
        save(data)
        if status == "deleted":
            log(f"{status}", tid)
        else: 
            log(f"marked {status}", tid)
    
    def ls(status):
        data = load()
        if status == "all":
            for i in data:
                print("{} {}\t{}\t{}".format(
                    i['tid'],
                    i['status'],
                    i['updateAt'],
                    i['detail'])) if i['status'] != "deleted" else 0
        else:
            for i in data:
                print("{} {}\t{}".format(
                    i['tid'],
                    i['updateAt'],
                    i['detail'])) if i['status'] == status else 0
class Task:
    def __init__(self, detail, tid):
        self.tid = tid
        self.detail = detail
        self.status = "todo"
        self.createAt = now()
        self.updateAt = now()

    def to_dict(self):
        return {
            "tid": self.tid,
            "detail": self.detail,
            "status": self.status,
            "createAt": self.createAt,
            "updateAt": self.updateAt
        }

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load():
    with open("log.json", 'r') as file:
        data = json.load(file)
    return data

def save(data):
    with open("log.json", 'w') as file:
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def log(change, tid):
    print(f"Task {change} (ID: {tid})")
