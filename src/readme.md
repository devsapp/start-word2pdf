## 简介

### 初始化

```bash
$ s init devsapp/start-word2pdf -d start-word2pdf
$ cd start-word2pdf
```

## 部署到函数计算

安装好 s 工具后，将 s.yaml 中的 Image 和 OSS 相关的环境变量改成您自己的，然后进行部署，部署完成之后，可以进行调用:

```bash
# 调用
$ s invoke -e '{"oss_file":"word2pdf/example.docx"}'
```

函数调用成功后，生成的 pdf 文件在和 docx 相同的 OSS 目录中，比如这个例子是在 word2pdf/example.pdf
