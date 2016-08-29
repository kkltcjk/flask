import json

class JsonParser():

    @classmethod
    def parse(self):
        with open('/tmp/yardstick.out') as f:
            lines = f.readlines()
            out_dict = {}
            result_list = []
            for index,line in enumerate(lines):
                    line_json = json.loads(line)
                    if index == 0:
                            out_dict["context"] = line_json
                    else:
                            result_list.append(line_json)
            out_dict["result"] = result_list
            return out_dict
