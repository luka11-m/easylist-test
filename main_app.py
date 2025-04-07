import streamlit as st

st.set_page_config(page_title="営業リスト作成ツール", layout="wide")
st.title("📞 営業リスト作成ツール（デモ）")

area = st.selectbox("地域を選択", ["渋谷区", "新宿区", "港区"])
industry = st.text_input("業種キーワード", value="住宅")

if st.button("検索開始"):
    st.success(f"検索キーワード：{area} + {industry}")
