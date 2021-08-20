## 简介

### 初始化

```bash
$ s init devsapp/start-word2pdf -d start-word2pdf
$ cd start-word2pdf
```

## 部署到函数计算

安装好 s 工具后，将 s.yaml 中的 OSS 相关的环境变量改成您自己的，然后:

```bash
$ s build --use-docker --dockerfile ./code/Dockerfile
$ s deploy --push-registry acr-internet --use-local -y

# 调用
$ s invoke -e '{"oss_file":"word2pdf/example.docx"}'
```

函数调用成功后，生成的 pdf 文件在和 docx 相同的 OSS 目录中，比如这个例子是在 word2pdf/example.pdf
