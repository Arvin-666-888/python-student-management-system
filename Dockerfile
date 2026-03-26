# 1. 选择基础镜像:Python 3.9 slim版(体积小、稳定，企业首选)
FROM python:3.9-slim

# 2. 设置工作目录:容器内的代码存放路径
WORKDIR /app

# 3. 复制依赖文件:先复制requirements.txt,利用Docker缓存加速构建
COPY requirements.txt .

# 4. 安装依赖:当前无依赖,预留步骤,后续扩展直接修改requirements.txt即可
RUN  pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 5. 复制项目代码:将本地所有代码复制到容器内
COPY . .

# 6. 声明数据卷:实施数据持久化,容器删除后students.json不丢失
VOLUME ["/app"]

# 7. 启动命令:运行学生管理系统主程序
CMD ["python","main.py"]