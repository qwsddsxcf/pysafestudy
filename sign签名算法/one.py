import hashlib
import time
import requests


def generate_sign():
    o = "12b6bb84e093532fb72b4d65fec3f00b"
    r = "/questions/lists"  # 注意：这里替换为当前请求的路径
    n = int(time.time() * 1000)  # 当前时间戳（毫秒）
    c = '2d203374-a4dc-496f-9372-21a16d55c641'  # 从 CLIENT-IDENTIFIER 获取

    # 拼接字符串 o + c + r + n + o
    data = o + c + r + str(n) + o

    # 计算 MD5
    h = hashlib.md5(data.encode('utf-8')).hexdigest()
    return h, n


def send_request():
    # 生成新的 sign 和时间戳
    new_sign, new_timestamp = generate_sign()

    # 请求头（基于提供的原始请求，更新 Sign 和 TimeStamp）
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "CLIENT-IDENTIFIER": "2d203374-a4dc-496f-9372-21a16d55c641",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "UM_distinctid=196dd3de83885b-0e8c32c09fd515-26001f51-19d826-196dd3de8391233; Hm_lvt_975400bd703f587eef8de1efe396089d=1747468544; HMACCOUNT=9ED92DCE4D49ADE8; uu=2d203374-a4dc-496f-9372-21a16d55c641; CNZZDATA1278923901=374368200-1747468544-%7C1747468583; Hm_lpvt_975400bd703f587eef8de1efe396089d=1747469649",
        "Host": "www.kaoshibao.com",
        "Origin": "https://www.kaoshibao.com",
        "Pragma": "no-cache",
        "REQUEST-ID": "5db83590-42dc-4cfa-835d-9ce8019b2b17",
        "Referer": "https://www.kaoshibao.com/online/paper/detail/?paperid=16882626",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sign": new_sign,  # 更新为新的 sign
        "TimeStamp": str(new_timestamp),  # 更新为新的时间戳
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "VERSION": "2.4.2",
        "platform": "web",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    # 请求体（假设是 JSON，根据实际情况调整）
    payload = {"paperid":"16882626","type":"all","size":10,"page":1} # 如果原始请求有 body，请替换为实际数据

    # 发送 POST 请求
    url = "https://www.kaoshibao.com/api/questions/lists"
    response = requests.post(url, headers=headers, json=payload)

    print("请求头中的 Sign:", new_sign)
    print("请求头中的 TimeStamp:", new_timestamp)
    print("响应状态码:", response.status_code)
    print("响应内容:", response.text)


if __name__ == "__main__":
    send_request()