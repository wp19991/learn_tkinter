import json


class json_database:
    def __init__(self, file_name=None):
        self.file_name = file_name
        with open(self.file_name, "r", encoding="utf-8") as f:
            self.data = json.loads(f.read())

    def write_data(self, web_name, account, password):
        info_list = {}
        info_list["web_name"] = web_name
        info_list["account"] = account
        info_list["password"] = password

        self.data.append(info_list)

        with open(self.file_name, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.data, ensure_ascii=False, indent=1))

    def show_info(self):
        web_list = []
        for info in self.data:
            web_list.append(info["web_name"])
        return web_list

    def show_AP(self, web_name):
        for info in self.data:
            if web_name == info["web_name"]:
                return info["account"], info["password"]
            else:
                continue

    def updata_info(self):
        new_web_list = []
        with open(self.file_name, "r", encoding="utf-8") as f:
            new_data = json.loads(f.read())
            for info in new_data:
                new_web_list.append(info["web_name"])
        return new_web_list
