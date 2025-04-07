import streamlit as st
import pandas as pd
from data_collector.google_search import google_search_companies
from data_collector.detail_parser import extract_info_from_url
from utils.io_handler import export_to_excel, export_to_google_sheets



st.set_page_config(page_title="営業リスト作成ツール", layout="wide")
st.title("📞 営業リスト作成ツール")

# 地域と業種の選択
area = st.selectbox("地域を選択", ["渋谷区", "新宿区", "港区"])
industry = st.text_input("業種キーワード", value="住宅")

# 検索ボタン
if st.button("検索開始"):
    st.success(f"検索キーワード：{area} + {industry}")

    # ① Google検索を実行
    search_results = google_search_companies(industry, area, max_results=5)

    # ② 各URLから詳細情報を取得
    detailed_results = []
    for r in search_results:
        detail = extract_info_from_url(r["url"])
        detail["タイトル"] = r["title"]
        detail["URL"] = r["url"]
        detailed_results.append(detail)

    # ③ 結果をDataFrameにして表示
    df = pd.DataFrame(detailed_results)
    st.dataframe(df)



