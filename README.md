# luna-voice
## 怎么食用

1. 从[我的百度网盘](https://pan.baidu.com/s/1P2XVahQcLuILjRbSfQRNvQ?pwd=1234)下载露娜的声音
2. 解压到wavs文件夹
3. 配置相关环境(cuda、TensorFlow、pytorch)
4. 下载NVIDIA的预训练模型[这里](https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing)
5. 放到文件夹
6. 打开train.ipynb训练
7. 下载NVIDIA的 [WaveGlow model](https://drive.google.com/open?id=1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF)
8. 打开 ./inference.ipynb 生成语音

## 文本和语音提取

使用[garbro](https://github.com/morkt/GARbro)和[asset studio](https://github.com/Perfare/AssetStudio)对近月1进行拆包

## 补充

作者4gb显存的显卡没扛住训练，希望有好心人继续训下去:cry:

8月11日，经群友点拨，只需修改./hparams.py 的batch_size即可，2的i次方调到能跑为止

![luna](./luna.jpg)



## 感谢

@[CjangCjengh](https://github.com/CjangCjengh/tacotron2-japanese/commits?author=CjangCjengh)的项目[CjangCjengh/tacotron2-japanese: Tacotron2 implementation of Japanese (github.com)](https://github.com/CjangCjengh/tacotron2-japanese))给了我能模拟出露娜大人的声音的机会

