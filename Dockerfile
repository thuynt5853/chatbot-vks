# Sử dụng image Python 3.8 chính thức
FROM rasa/rasa-sdk:3.6.0

USER root

# Cập nhật hệ thống và cài đặt các gói cần thiết
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER 1001

# Cài đặt pip và các công cụ hữu ích
RUN python -m pip install --upgrade pip setuptools wheel

# Tạo thư mục làm việc và sao chép các tệp của dự án vào container
WORKDIR /app
FROM rasa/rasa-sdk:3.6.0

WORKDIR /app
COPY ./actions /app/actions
COPY ./requirements.txt /app/requirements.txt

RUN pip install --root  --no-cache-dir -r requirements.txt

# Cài đặt Rasa, Langchain, Gradio, Hugging Face
#RUN pip install rasa langchain gradio transformers
#rUN pip install --no-cache-dir torch torchvision torchaudio

# Mở cổng 5005 cho Rasa
#EXPOSE 5005

# Lệnh chạy khi container khởi động
#CMD ["rasa", "run", "--enable-api", "--cors", "*"]
