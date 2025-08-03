# Sử dụng image NVIDIA CUDA với Ubuntu 22.04 làm base
FROM nvidia/cuda:12.4.0-base-ubuntu22.04

# Cài đặt Python 3.10 và pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập thư mục làm việc là /app
WORKDIR /app

# Sao chép toàn bộ nội dung thư mục hiện tại vào /app trong container
COPY . /app

# Cài đặt các dependencies nếu có requirements.txt
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Mở bash khi chạy container
CMD ["/bin/bash"]