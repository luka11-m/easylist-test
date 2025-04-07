import requests
from bs4 import BeautifulSoup
import re

def extract_info_from_url(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()

        data = {
            "会社名": soup.title.string.strip() if soup.title else "",
            "電話番号": None,
            "住所": None,
            "SNS": []
        }

        # 電話番号の抽出
        phone_match = re.search(r'(0\d{1,4}-\d{1,4}-\d{3,4})', text)
        if phone_match:
            data["電話番号"] = phone_match.group()

        # 住所の抽出（都道府県＋市区町村）
        address_match = re.search(r'.{0,10}[都道府県].{1,20}[市区町村].{0,30}', text)
        if address_match:
            data["住所"] = address_match.group()

        # SNSリンクの抽出
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "instagram.com" in href or "youtube.com" in href:
                data["SNS"].append(href)

        return data

    except Exception as e:
        return {"error": str(e), "url": url}

