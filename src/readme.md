#  阿里云函数计算 Word2Pdf 案例

> 快速部署和体验 Serverless 架构下的 Word 转 PDF 案例

- [阿里云函数计算 Word2Pdf 案例](#阿里云函数计算-word2pdf-案例)
  - [体验前准备](#体验前准备)
  - [代码](#代码)
  - [快速部署和体验](#快速部署和体验)
    - [在线快速体验](#在线快速体验)
    - [在本地部署体验](#在本地部署体验)
    - [调用函数](#调用函数)

## 体验前准备

该应用案例，需要您开通[阿里云函数计算](https://fcnext.console.aliyun.com/) 产品；并建议您当前的账号有权限存在`FCDefaultRole`。

## 代码

- [:octocat: 源代码](https://github.com/devsapp/start-word2pdf/tree/main/src)

## 快速部署和体验
### 在线快速体验

- 通过阿里云 **Serverless 应用中心**： 可以点击 [【🚀 部署】](https://fcnext.console.aliyun.com/applications/create?template=start-word2pdf) ，按照引导填入参数，快速进行部署和体验。

### 在本地部署体验

1. 下载安装 Serverless Devs：`npm install @serverless-devs/s` 
    > 详细文档可以参考 [Serverless Devs 安装文档](https://github.com/Serverless-Devs/Serverless-Devs/blob/master/docs/zh/install.md)
2. 配置密钥信息：`s config add`
    > 详细文档可以参考 [阿里云密钥配置文档](https://github.com/devsapp/fc/blob/main/docs/zh/config.md)
3. 初始化项目：`s init start-word2pdf -d start-word2pdf`
4. 进入项目并部署：`cd start-word2pdf && s deploy`

### 调用函数

```bash
# 调用
$ s invoke -e '{"oss_file":"word2pdf/example.docx"}'
```

函数调用成功后，生成的 pdf 文件在和 docx 相同的 OSS 目录中，比如这个例子是在 word2pdf/example.pdf。通过 Serverless Devs 开发者工具，您只需要几步，就可以体验 Serverless 架构带来的降本提效的技术红利。

-----

> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs   
> - Serverless Devs 文档：https://www.github.com/serverless-devs/docs   
> - Serverless Devs 钉钉交流群：33947367    
