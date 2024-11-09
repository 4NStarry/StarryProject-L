## 基于PySide6的工程结构震害照片辅助贴标软件 ##

StarryProject-L能够帮助用户基于图像内容操作生成大模型训练所需的与之对齐的文本。其核心理念在于生成与大型语言模型之间的精准对齐的JSON文本对，以便数据集训练后的大模型实现图像与文本间的无缝转换。

您的计算机必须满足下列前置条件才能运行此系列软件：
- Ｐｙｔｈｏｎ３
- ＰｙＳｉｄｅ６

目前程序(截止Ｖ１.４.２)未修复ＢＵＧ：

- check4,5启用逻辑，必须「有损伤」被选中的情况下。
- 「整体」下无明显损伤　生成错误文本。
- 「整体」下清除文件无提示。
- 破坏程度可以有损伤时默认轻微
- display函数name应从「.jpg」截断而非「.」，写入json应用新'f{raw}.json'
- 「楼板」在写入ＪＳＯＮ时没有被正确替换

暂时没时间修复所以很抱歉^^;