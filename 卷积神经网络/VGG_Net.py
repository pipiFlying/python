"""
搭建 VGG 网络

添加 Dropout 抑制神经元，减少神经元参数和增加丰富度，用于全连接网络

BatchNorm2d 用于卷积网络优化作用

nn.AdaptiveAvgPool2d((7, 7))，标准化处理后应 <= 10 * 10 常规就是 7 * 7

"""
import torch.nn as nn
import torch

# from torchvision import models
#
# models.VGG

class VGGNet(nn.Module):
    def __init__(self, features, dropout=0.5, num_classes=1000):
        super().__init__()
        # 卷积层
        self.features = features
        self.avg_pool = nn.AdaptiveAvgPool2d((7, 7))
        # 全连接层
        self.classifier = nn.Sequential(
            nn.Linear(in_features=7 * 7 * 512, out_features=4096),
            nn.ReLU(inplace=True),
            # 添加 Dropout 抑制神经元，减少神经元参数和增加丰富度，用于全连接网络
            nn.Dropout(dropout),
            nn.Linear(in_features=4096, out_features=4096),
            nn.ReLU(inplace=True),
            # 添加 Dropout 抑制神经元，减少神经元参数和增加丰富度，用于全连接网络
            nn.Dropout(dropout),
            nn.Linear(in_features=4096, out_features=num_classes),
        )

    def forward(self, x):
        # 卷积层处理
        x = self.features(x)
        # 指定输出大小 7 * 7
        x = self.avg_pool(x)
        # 数据展平 (N, C, H, W) -> (N, V)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

cfgs = {
    "A": [64, "M", 128, "M", 256, 256, "M", 512, 512, "M", 512, 512, "M"],
    "B": [64, 64, "M", 128, 128, "M", 256, 256, "M", 512, 512, "M", 512, 512, "M"],
    "D": [64, 64, "M", 128, 128, "M", 256, 256, 256, "M", 512, 512, 512, "M", 512, 512, 512, "M"],
    "E": [64, 64, "M", 128, 128, "M", 256, 256, 256, 256, "M", 512, 512, 512, 512, "M", 512, 512, 512, 512, "M"],
}

def make_layers(cfg, batch_norm: bool = False):
    layers = []
    in_channels = 3
    for v in cfg:
        if v == "M":
            # 添加池化
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            # 创建卷积
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            if batch_norm:
                # BatchNorm2d 用于卷积网络优化作用
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
    return nn.Sequential(*layers)

def vgg11():
    return VGGNet(make_layers(cfgs["A"]))

def vgg13():
    return VGGNet(make_layers(cfgs["B"]))

def vgg16():
    return VGGNet(make_layers(cfgs["D"]))

def vgg19():
    return VGGNet(make_layers(cfgs["E"]))

__all__ = ['vgg11']



