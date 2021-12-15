async function preInit(inputObj) {
    console.log(`\n                            .___________            .___ _____ 
    __  _  _____________  __| _/\\_____  \\______   __| _// ____\\
    \\ \\/ \\/ /  _ \\_  __ \\/ __ |  /  ____/\\____ \\ / __ |\\   __\\ 
     \\     (  <_> )  | \\/ /_/ | /       \\|  |_> > /_/ | |  |   
      \\/\\_/ \\____/|__|  \\____ | \\_______ \\   __/\\____ | |__|   
                         \\/         \\/__|        \\/        `)
}

async function postInit(inputObj) {
    console.log(`\n    Welcome to the start-bottle application
     This application requires to open these services: 
         FC : https://fc.console.aliyun.com/
         ACR: https://cr.console.aliyun.com/
         OSS: https://oss.console.aliyun.com/
     
     * 额外说明：
        1. 完成项目初始化之后，需要在s.yaml中进行相关内容的配置：
           - 在environmentVariables参数下，配置对象存储相关的信息
           - 在customContainerConfig参数下，配置容器镜像相关信息
     * 完成上述操作之后，可使用 s deploy 进行项目部署
     * 可以通过invoke命令进行相关的触发：s invoke -e '{"oss_file":"word2pdf/example.docx"}'\n`)
}

module.exports = {
    postInit,
    preInit
}
