"""
python 解析 yaml 文件

    需要安装 pyyaml
    - 使用 conda 安装
    conda install pyyaml

    yaml.load()
    yaml.dump()
"""

import yaml

with open("config.yaml", 'r', encoding='utf-8') as fr:
    # yaml.FullLoader 完整加载，会加载代码
    # yaml.SafeLoader 安全加载，不会执行代码，达到安全效果
    obj = yaml.load(fr, Loader=yaml.FullLoader)
    print(obj)
    print(obj['services']['sms_service'])