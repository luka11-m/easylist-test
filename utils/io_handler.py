import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def export_to_excel(df, filename_prefix="営業リスト"):
    date_str = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{filename_prefix}_{date_str}.xlsx"
    df.to_excel(filename, index=False, engine='openpyxl')
    return filename

def export_to_google_sheets(df, sheet_name="営業リスト"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # 新しいスプレッドシート作成
    sheet = client.create(sheet_name)
    ws = sheet.get_worksheet(0)
    ws.update([df.columns.values.tolist()] + df.values.tolist())
    return sheet.url
