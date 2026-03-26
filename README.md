面向对象学生管理系统

Python企业级实战项目 | 求职简历必备 | 全功能完整版

🎯 项目介绍

本项目是一个基于 Python 面向对象编程（OOP）​ 思想开发的标准化学生信息管理系统。它严格遵循 PEP8 代码规范​ 与 企业级工程化​ 开发理念，实现了学生信息的全生命周期管理。

系统核心特点是无第三方依赖、开箱即用、安全稳定，是巩固 Python 基础、学习软件开发流程及丰富个人简历的绝佳实战项目。

🛠️ 技术栈

核心语言: Python 3.9 \~ 3.12

核心技术: 面向对象编程（OOP）、模块化设计、异常处理

数据存储: 本地 JSON 文件（实现数据持久化）

核心规范: PEP8 代码规范、Git 版本管理、详尽注释、用户友好交互

💡 核心功能

学生信息新增：支持录入姓名、年龄、学号（唯一标识）。

学生信息查询：支持全量列表展示与按姓名精准查询。

学生信息修改：支持更新学生姓名、年龄等信息。

学生信息删除：支持按姓名删除指定学生记录。

数据持久化：所有数据通过 JSON 文件存储，程序重启后数据不丢失。

异常安全防护：对文件读写异常、用户输入异常等进行全面捕获与处理，保证程序健壮性，永不崩溃。

控制台菜单交互：提供简洁直观的文本菜单，操作指引清晰。

🚀 运行步骤

方式一:本地Python运行

按照以下步骤，即可在本地运行本项目：

克隆仓库到本地

bash
复制
git clone https://github.com/Arvin-666-888/python-student-management-system.git

进入项目目录

bash
复制
cd python-student-management-system

运行主程序

bash
复制
python main.py

随后，程序将启动并显示交互菜单，您可以根据提示进行各项操作。

方式二:Docker一键运行

克隆本仓库到本地

bash
复制
git clone https://github.com/Arvin-666-888/python-student-management-system.git

进入项目目录

bash
复制
cd python-student-management-system

构建Docker镜像

bash
复制
docker build -t student-system:v1

运行容器(带数据持久化)

bash
复制
# Windows PowerShell

docker run -it --name student-container -v ${PWD}:/app student-system:v1



📁 项目结构
复制
python-student-management-system/
├── main.py              # 项目主程序，包含所有核心功能与交互逻辑
├── students.json        # 数据持久化文件（首次运行后自动生成）
├── .gitignore           # Git版本管理忽略配置文件
└── README.md            # 项目说明文档（本文档）
🤝 贡献

欢迎提交 Issues 和 Pull Requests 来帮助改进此项目。

