import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import secrets
import hashlib
import random

# Danh sách từ BIP39 tiếng Anh (2048 từ)
BIP39_WORDS = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse",
    "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act",
    "action", "actor", "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit",
    "adult", "advance", "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
    "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter",
    "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger",
    "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
    "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april", "arch", "arctic",
    "area", "arena", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest",
    "arrive", "arrow", "art", "artefact", "artist", "artwork", "ask", "aspect", "assault", "asset",
    "assist", "assume", "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction",
    "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake",
    "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge",
    "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain"
]

def generate_mnemonic():
    # Tạo 12 từ ngẫu nhiên từ danh sách BIP39
    return " ".join(random.sample(BIP39_WORDS, 12))

def generate_private_key(mnemonic):
    # Tạo private key từ mnemonic bằng cách hash
    return hashlib.sha256(mnemonic.encode()).hexdigest()

def generate_address(private_key):
    # Tạo địa chỉ ví đơn giản từ private key
    address = hashlib.sha256(private_key.encode()).hexdigest()
    return f"0x{address[:40]}"  # Lấy 40 ký tự đầu và thêm tiền tố 0x

def generate_wallet():
    # Tạo mnemonic
    mnemonic = generate_mnemonic()
    
    # Tạo private key
    private_key = generate_private_key(mnemonic)
    
    # Tạo địa chỉ ví
    address = generate_address(private_key)
    
    # Lưu thông tin vào file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'wallet_info_{0xA0D068926eE7136362EaBE8148cbCF5143DB0519}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'CẢNH BÁO: KHÔNG CHIA SẺ THÔNG TIN NÀY VỚI BẤT KỲ AI!\n')
        f.write(f'Mnemonic (Cụm từ ghi nhớ): {mnemonic}\n')
        f.write(f'Private Key (Khóa bí mật): {private_key}\n')
        f.write(f'EVM Address (Địa chỉ ví): {address}')
    
    return address

class WalletGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tạo Ví Tiền Mã Hóa")
        self.root.geometry("600x400")
        
        # Tạo style cho giao diện
        style = ttk.Style()
        style.configure('TButton', padding=10)
        style.configure('TLabel', padding=5)
        
        # Tạo các widget
        self.create_widgets()
    
    def create_widgets(self):
        # Tiêu đề
        title_label = ttk.Label(
            self.root,
            text="Chương Trình Tạo Ví Tiền Mã Hóa",
            font=("Helvetica", 16)
        )
        title_label.pack(pady=20)
        
        # Nút tạo ví mới
        generate_button = ttk.Button(
            self.root,
            text="Tạo Ví Mới",
            command=self.generate_new_wallet
        )
        generate_button.pack(pady=10)
        
        # Label hiển thị địa chỉ
        self.address_label = ttk.Label(
            self.root,
            text="Địa chỉ ví sẽ hiển thị ở đây",
            wraplength=500
        )
        self.address_label.pack(pady=10)
        
        # Label thông báo
        self.info_label = ttk.Label(
            self.root,
            text="",
            wraplength=500
        )
        self.info_label.pack(pady=10)
    
    def generate_new_wallet(self):
        # Tạo ví mới và hiển thị địa chỉ
        address = generate_wallet()
        self.address_label.config(text=f"Địa chỉ ví của bạn:\n{address}")
        
        # Hiển thị thông báo
        self.info_label.config(
            text=f"Đã lưu thông tin ví vào thư mục hiện hành.\n"
                 f"Vui lòng giữ an toàn file thông tin ví!"
        )

if __name__ == "__main__":
    # Khởi tạo ứng dụng
    root = tk.Tk()
    app = WalletGeneratorApp(root)
    root.mainloop()