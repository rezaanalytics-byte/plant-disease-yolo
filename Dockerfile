# استفاده از ایمیج آماده و سنگین اولترالیتیکس (همه چیز از قبل نصب است)
FROM ultralytics/ultralytics:latest

WORKDIR /app

# فقط کتابخانه‌های سبک API را نصب می‌کنیم (بسیار سریع)
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]