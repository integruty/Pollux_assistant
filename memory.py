import json, os

class Memory:
    def __init__(self):
        self.file = "memory.json"
        if not os.path.exists(self.file):
            with open(self.file,"w") as f:
                json.dump([], f)

    def add(self, role, text):
        data = self.load()
        data.append({"role":role,"text":text})
        with open(self.file,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)

    def load(self):
        with open(self.file,"r",encoding="utf-8") as f:
            return json.load(f)