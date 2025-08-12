import yaml

def parse_yaml(path):
    with open(path, mode='r+', encoding='utf-8') as fr:
        obj = yaml.safe_load(fr)
        return obj

def write_yaml(path, obj):
    with open(path, mode='w', encoding='utf-8') as fw:
        # default_flow_style 默认: 流式
        yaml.safe_dump(obj, fw, default_flow_style=False, allow_unicode=True)

if __name__ == '__main__':
    obj = {
        'user': {
            'id': 1,
            'name': 'libai',
            'age': 20
        }
    }
    write_yaml('test_r.yaml', obj)