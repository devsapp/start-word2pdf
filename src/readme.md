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

# 代码 & 预览

- [😼 源代码](https://github.com/devsapp/start-word2pdf)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- 🔥 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-word2pdf) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-word2pdf)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：\`s init start-word2pdf -d start-word2pdf\`   
    - 进入项目，并进行项目部署：\`cd start-word2pdf && s deploy -y\`

</deploy>

<appdetail id="flushContent">

# 应用详情

项目部署完成，可以通过`invoke`命令进行触发/测试：

```bash
# 调用
$ s invoke -e '{"oss_file":"word2pdf/example.docx"}'
```

函数调用成功后，生成的 pdf 文件在和 docx 相同的 OSS 目录中，比如这个例子是在 word2pdf/example.pdf。

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：\`serverless\`</center> | <center>微信小助手：\`xiaojiangwh\`</center> | <center>钉钉交流群：\`33947367\`</center> | 

</p>

</devgroup>