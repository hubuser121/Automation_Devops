WORKDIR /app
COPY requirements.txt .    # Copy only requirements.txt first
RUN pip install -r requirements.txt
COPY . .                  # Copy remaining files
CMD ["python", "app.py"]
