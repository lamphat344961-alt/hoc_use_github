import requests

url = "http://127.0.0.1:8000/predict"

# Dữ liệu người dùng nhập
data = {
    "age": 30,
    "income": 5000,
    "loan_amount": 8000
}

response = requests.post(url, json=data)

print("📤 Data gửi đi:", data)
print("📥 Kết quả trả về:", response.json())
