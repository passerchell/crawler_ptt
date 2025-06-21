# 使用 Python 官方精簡映像
FROM python:3.10-slim

# 建立工作目錄
WORKDIR /app

# 複製 pyproject.toml
COPY pyproject.toml poetry.lock* /app/

# 安裝 Poetry
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

# 複製程式碼
COPY . .

# 預設執行命令（依實際 entry point 調整）
CMD ["python", "main.py"]
