# Writup of 2025 TSCCTF

> 2025-01-13 - 2025-01-16

## WELCOME

### Give you a free flag

![Solution](https://hackmd.io/_uploads/Syx6hhQP1e.png =400x)

下面空白這麼多看起來就有問題，選取看看，果真有字。
- Flag: `TSC{W3llc0me_t0_TSC2O2SIlIllI}`

### Please Join our Discord!!!

> Unlock Hint for 0 points
> Emoji 是 TSCCTF2024 的 DC flag !

Hint 說 emoji 是 2024 的，意思是不要找錯，但我誤以為要找那個，甚至開了一張 ticket 去問，總之真正的 flag 其實埋在公告頻道的說明裡面，如下圖
![Solution](https://hackmd.io/_uploads/ryHw4eEPJe.png)
- Flag：`TSC{w31c0m3_t0_s5cc7f2025_d15c0rd!!!}`

### Feedback Form

填寫回饋表單拿 50 分
- Flag: `TSC{thanks_for_playing_and_c_u_nexy_year!}`

## PWN

### gamble_bad_bad

> `./gamble_bad_bad/main.cpp`
```cpp=
#include <string.h>
#include <iostream>
#include <stdio.h>
using namespace std;

void jackpot() {
    char flag[50];
    FILE *f = fopen("/home/gamble/flag.txt", "r");
    if (f == NULL) {
        printf("錯誤：找不到 flag 檔案\n");
        return;
    }
    fgets(flag, 50, f);
    fclose(f);
    
    printf("恭喜你中了 777 大獎！\n");
    printf("Flag 是：%s", flag); 
}

struct GameState {
   char buffer[20];
   char jackpot_value[4];  
} game;

void spin() {
   strcpy(game.jackpot_value, "6A6");
   
   printf("輸入你的投注金額：");
   gets(game.buffer);

   printf("這次的結果為：%s\n", game.jackpot_value);

   if (strcmp(game.jackpot_value, "777") == 0) {
       jackpot();
   } else {
       printf("很遺憾，你沒中獎，再試一次吧！\n");
   }
}

int main() {
   setvbuf(stdout, NULL, _IONBF, 0);
   setvbuf(stdin, NULL, _IONBF, 0);
   printf("歡迎來到拉霸機！試著獲得 777 大獎吧！\n");
   spin();
   return 0;
}
```

目標是觸發 `jackpot` 函式，觸發條件為將 `game.jackpot_value` 的值從 `6A6` 改為 `777`。
程式在第 29 行使用了 `gets`，並沒有檢查輸入字串長度，因此可以從 `game.buffer` 蓋到 `game.value`，`game.buffer` 大小為 20 個 byte，因此輸入隨意 20 個字元後面再接 `777` 即可竄改 `game.value` 數值。
解法如下圖：輸入 `00000000000000000000777`，得到 flag 為 `TSC{Gamble_Very_bad_bad_but_}`

![Solution](https://hackmd.io/_uploads/rJpsp2mvJe.png =600x)

## CRYPTO

### Very Simple Login

> `./very-simple-login/server.py`
```python=
import base64
import hashlib
import json
import os
import re
import sys
import time
from secret import FLAG


def xor(message0: bytes, message1: bytes) -> bytes:
    return bytes(byte0 & byte1 for byte0, byte1 in zip(message0, message1))


def sha256(message: bytes) -> bytes:
    return hashlib.sha256(message).digest()


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    blocksize = 64
    if len(key) > blocksize:
        key = sha256(key)
    if len(key) < blocksize:
        key = key + b'\x00' * (blocksize - len(key))
    o_key_pad = xor(b'\x5c' * blocksize, key)
    i_key_pad = xor(b'\x3c' * blocksize, key)
    return sha256(o_key_pad + sha256(i_key_pad) + message)


def sha256_jwt_dumps(data: dict, exp: int, key: bytes):
    header = {'alg': 'HS256', 'typ': 'JWT'}
    payload = {'sub': data, 'exp': exp}
    header = base64.urlsafe_b64encode(json.dumps(header).encode())
    payload = base64.urlsafe_b64encode(json.dumps(payload).encode())
    signature = hmac_sha256(key, header + b'.' + payload)
    signature = base64.urlsafe_b64encode(signature).rstrip(b'=')
    return header + b'.' + payload + b'.' + signature


def sha256_jwt_loads(jwt: bytes, exp: int, key: bytes) -> dict | None:
    header_payload, signature = jwt.rsplit(b'.', 1)

    sig = hmac_sha256(key, header_payload)
    sig = base64.urlsafe_b64encode(sig).rstrip(b'=')
    if sig != signature:
        raise ValueError('JWT error')

    try:
        header, payload = header_payload.split(b'.')[0], header_payload.split(b'.')[-1]
        header = json.loads(base64.urlsafe_b64decode(header))
        payload = json.loads(base64.urlsafe_b64decode(payload))
        if (header.get('alg') != 'HS256') or (header.get('typ') != 'JWT'):
            raise ValueError('JWT error')
        if int(payload.get('exp')) < exp:
            raise ValueError('JWT error')
    except Exception:
        raise ValueError('JWT error')
    return payload.get('sub')


def register(username: str, key: bytes):
    if re.fullmatch(r'[A-z0-9]+', username) is None:
        raise ValueError("'username' format error.")
    return sha256_jwt_dumps({'username': username}, int(time.time()) + 86400, key)


def login(token: bytes, key: bytes):
    userdata = sha256_jwt_loads(token, int(time.time()), key)
    return userdata['username']


def menu():
    for _ in range(32):
        print('==================')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        try:
            choice = int(input('> '))
        except Exception:
            pass
        if 1 <= choice <= 3:
            return choice
        print('Error choice !', end='\n\n')
    sys.exit()


def main():
    key = os.urandom(32)
    for _ in range(32):
        choice = menu()
        if choice == 1:
            username = input('Username > ')
            try:
                token = register(username, key)
            except Exception:
                print('Username Error !', end='\n\n')
                continue
            print(f'Token : {token.hex()}', end='\n\n')
        if choice == 2:
            token = bytes.fromhex(input('Token > '))
            try:
                username = login(token, key)
            except Exception:
                print('Token Error !', end='\n\n')
            if username == 'Admin':
                print(f'FLAG : {FLAG}', end='\n\n')
                sys.exit()
            else:
                print('FLAG : TSC{???}', end='\n\n')
        if choice == 3:
            sys.exit()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()
```

目標是觸發第 107 行印出 flag，觸發條件為 `username='Admin'`。
可以透過選項 1 創建 username 為 `Admin` 的用戶，得到 Token 後，再透過選項 2 將得到的 token 帶入，即可以 Admin 身分登入，獲得 flag，解法如下圖：
![Solution](https://hackmd.io/_uploads/SyLU1TmD1g.png)
不過我認為這題跟 crypto 無關就是了。。

### Classic

> `./classic/chal.py`
```python=
import os
import string
import secrets

flag = os.getenv("FLAG") or "TSC{test_flag}"

charset = string.digits + string.ascii_letters + string.punctuation
A, B = secrets.randbelow(2**32), secrets.randbelow(2**32)
assert len(set((A * x + B) % len(charset) for x in range(len(charset)))) == len(charset)

enc = "".join(charset[(charset.find(c) * A + B) % len(charset)] for c in flag)
print(enc)
```

> flag
```txt=
o`15~UN;;U~;F~U0OkW;FNW;F]WNlUGV"
```

題目給了加密流程以及加密後的 flag，過程是用 affine encoding 加密，很明顯就是如果我能透過 affine decode 就能得到 flag。
看題目，如果我能拿到兩個 32-bit 的隨機數 `A` 和 `B`，就能把 flag 解出來，暴力解需要 (2^{32})^2 = 2^{64}，而剛好其實暴力解滿快就得到答案

> `./classic/exp.py`
```python=
import string
from math import gcd
import secrets

# Define the charset
charset = string.digits + string.ascii_letters + string.punctuation
N = len(charset)

# Find the modular multiplicative inverse of A
def mod_inverse(A, N):
    for i in range(N):
        if (A * i) % N == 1:
            return i
    return -1

while True:
    A = secrets.randbelow(2**32)

    A_inv = mod_inverse(A, N)

    if A_inv == -1:
        continue
    
    B = secrets.randbelow(2**32)

    # Encrypted message (replace with the actual encrypted string)
    with open("flag", "r") as file:
        encrypted_message = file.readline()

    # Decrypt the message
    decrypted_message = ""
    for c in encrypted_message:
        y = charset.find(c)  # Get the index of the encrypted character
        x = (A_inv * (y - B)) % N  # Apply decryption formula
        decrypted_message += charset[x]  # Map back to the original character
    if "TSC{" in decrypted_message:
        print(f"A={A}")
        print(f"B={B}")
        print("Decrypted message:", decrypted_message)
        exit()
```

![Solution](https://hackmd.io/_uploads/rJlBxaQwkg.png)

---

# 結果

> Scoreboard: 162 / 509

![Scoreboard](https://hackmd.io/_uploads/BJETh7IDJg.png)

> Qualified Scoreboard: about 20 / 36

![Qualified Scoreboard](https://hackmd.io/_uploads/rk4a37LPkl.png)

---

# 心得

終於打到一場可以破蛋的 CTF？有感受到 TSC 想要破除賽棍詛咒 && 給予新手友善環境的比賽，因為有些題目連我都可以打得出來所以很明顯感受到**友善**和難易度的變化

回想一下 CTF 一路上的問題：
- MISC 的題目已經連續兩次遇到 pyjail，但都解不出來，好像沒有很深入的了解 pyjail 的概念
- REVERSE 都會拿 ghidra 和 ida 出來逆，也可以看懂一點點程式的邏輯，但都沒能持續往下解到最後一步驟
- PWN 好像也是沒有往下解
- WEB 一直不懂起手式在哪裡，看到沒有任何輸入的題目就只會想著 F12 看原始碼、看 cookie 和 local storage，不然就是 URL 直接加 `/flag` 下去，沒有其他手段了
- CRYPTO 應該就是對很多密碼學概念不熟悉，所以不太會願意往下鑽研

可以期待之後其他人寫的 writeup，看看還有解的題目 solution 長什麼樣子
