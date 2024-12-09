# 使用 Python 3.11 作为基础镜像
FROM python:3.11

# 暴露 Streamlit 的默认端口（8080）
EXPOSE 8080

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有内容到容器的工作目录
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置容器启动时运行的命令
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]