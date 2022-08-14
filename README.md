# luna-voice
## 怎么训练

1. 从我的百度网盘下载露娜的声音
2. 解压到wavs文件夹
3. 配置相关环境(cuda、TensorFlow、pytorch)
4. 下载NVIDIA的预训练模型[这里](https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing)
5. 放到文件夹
6. 打开train.ipynb训练

## 怎么生成语音

1. 下载NVIDIA的 [WaveGlow model](https://drive.google.com/open?id=1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF)
2. 可以使用epoch为100的[模型]()，也可以自己训练
3. 打开 ./inference.ipynb ，修改模型路径，生成语音

## 文本和语音提取

使用[garbro](https://github.com/morkt/GARbro)和[asset studio](https://github.com/Perfare/AssetStudio)对近月1进行拆包

所有资源均已分享到[百度网盘](https://pan.baidu.com/s/1X0oT8_IPQJ9Tcp_Po3VN-A?pwd=1234)

## 补充

~~作者4gb显存的显卡没扛住训练，希望有好心人继续训下去~~:cry:

8月11日，经群友点拨，只需修改./hparams.py 的batch_size即可，2的i次方调到能跑为止

![luna](./luna.jpg)

8月14日，嫖了张A5000，终于训完了，个人感觉效果还可以

## 感谢

@[CjangCjengh](https://github.com/CjangCjengh/tacotron2-japanese/commits?author=CjangCjengh)的项目[CjangCjengh/tacotron2-japanese: Tacotron2 implementation of Japanese (github.com)](https://github.com/CjangCjengh/tacotron2-japanese))给了我能模拟出露娜大人的声音的机会

