# Sử dụng image Rasa SDK chuẩn
FROM rasa/rasa-sdk:3.6.0

# Tùy chọn chuyển qua root nếu bạn cần cài thêm gói hệ thống (có thể giữ lại hoặc bỏ)
USER root

# (Tùy chọn) Cài thêm các gói hệ thống cần thiết — chỉ khi bạn thực sự cần
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Quay lại user không phải root để an toàn


# Tạo thư mục làm việc
WORKDIR /app

# Copy thư mục actions và file requirements vào image
COPY ./actions /app/actions
COPY ./actions/requirements.txt /app


# Cài đặt các thư viện Python cần thiết
RUN pip install --no-cache-dir -r /app/requirements.txt



USER 1001
# Mặc định chạy action server khi container khởi động
#CMD ["python", "-m", "rasa_sdk.endpoint", "--actions", "actions"]
CMD ["python", "-m", "rasa_sdk.endpoint", "--actions", "actions"]


#CMD ["rasa", "run", "actions"]


EXPOSE 5055


