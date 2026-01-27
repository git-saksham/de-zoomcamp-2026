FROM python:3.13-slim
RUN pip install pandas pyarrow fastparquet
WORKDIR /app
COPY solution.py .
ENTRYPOINT ["python", "solution.py"]