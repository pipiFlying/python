import json

def json_parse(path):
    with open(path, mode='r+', encoding='utf-8') as f_r:
        data = json.load(f_r)
        return data

def json_write(path, data):
    with open(path, mode='w+', encoding='utf-8') as f_w:
        # ensure_ascii=False 表示内容不转换成 ascii
        json.dump(data, f_w, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    pass