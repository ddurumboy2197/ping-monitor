import secrets
import string

def generate_otp(length=6):
    """OTPni yaratish uchun funksiya"""
    return ''.join(secrets.choice(string.digits) for _ in range(length))

def verify_otp(otp, user_otp):
    """OTPni tekshirish uchun funksiya"""
    return otp == user_otp

# OTP yaratish
otp = generate_otp()
print(f"OTP: {otp}")

# OTPni tekshirish
user_otp = input("Iltimos, OTPni kiriting: ")
if verify_otp(otp, user_otp):
    print("OTP muvaffaqiyatli tekshirildi!")
else:
    print("OTP noto'g'ri!")
```

Kodni ishlatish uchun quyidagicha:

1. `generate_otp()` funksiyasini boshlash uchun `generate_otp()` funksiyasini chaqiring.
2. OTPni yaratish uchun `generate_otp()` funksiyasidan foydalaning.
3. OTPni tekshirish uchun `verify_otp()` funksiyasidan foydalaning.
4. `verify_otp()` funksiyasiga OTPni kiriting.
5. OTP muvaffaqiyatli tekshirilganligini tekshiring.
