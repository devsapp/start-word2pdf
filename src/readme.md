# start-word2pdf 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-word2pdf&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-word2pdf" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-word2pdf&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-word2pdf" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-word2pdf&type=packageDownload">
  </a>
</p>

<description>

> ***快速部署一个word转pdf的应用到阿里云函数计算***

</description>

<table>
</table>

<codepre id="codepre">
</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-word2pdf) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-word2pdf)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-word2pdf -d start-word2pdf`   
    - 进入项目，并进行项目部署：`cd start-word2pdf && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

项目部署完成，可以通过`invoke`命令进行触发/测试：

```bash
# 调用
$ s invoke -e '{"word_file":"example.docx"}'
```

函数调用成功后，生成的 pdf 文件在和 docx 相同的 OSS 目录中，比如这个例子是在 example.pdf。

如果您想 word 转 pdf 同时再加上水印， 需要增加如下相关的参数：

```
{
    "word_file": "example.docx",  
    "mark_text": "AliyunFC",  // 水印文字， 如果给 PDF 加水印，该参数必填
    "pagesize": [595.275590551181, 841.8897637795275], // 可选参数，默认是 A4 大小， (21*cm, 29.7*cm), 其中 1cm=28.346456692913385
    "font": "Helvetica", // 字体，可选参数， 默认为 Helvetica,  中文字体可选择为 zenhei 或 microhei
    "font_size": 30, // 字体d大小，可选参数， 默认为 30
    "font_color": [0, 0, 0], // 字体颜色，格式为 RGB， 默认为黑色
    "rotate": 30, // 旋转角度, 可选参数， 默认为 0
    "opacity": 0.1, // 透明度, 可选参数， 默认为 0.1， 1 表示不透明
    "density": [198.4251968503937, 283.46456692913387] // 水印密度，水印文字间隔，默认是 [141.73228346456693, 141.73228346456693]，即（7*cm, 10*cm),  表示每个水印文字在横坐标和纵坐标的间隔分别是 7cm 和 10cm
}
```

比如:
```bash
$ s invoke -e '{"word_file":"example.docx", "mark_text": "AliyunFC", "rotate":30}'

# 如果是中文水印, font 为 zenhei 或者 microhei
$ s invoke -e '{"word_file":"example.docx", "mark_text": "函数计算", "rotate":30, "font": "zenhei"}'
```

生成带有水印的 example.pdf 示例:
    
![](https://img.alicdn.com/imgextra/i4/O1CN01xJymEK1MP9YHRBkQx_!!6000000001426-2-tps-652-841.png)

# 其他
如果进行二次开发， 有新的依赖 python lib, 可以直接使用如下命令：

```bash
$ s build --use-sandbox
# 进入 sandbox 后
$ s-install pip install xxx

# exit 退出， 然后重新 s deploy 即可
```

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>
