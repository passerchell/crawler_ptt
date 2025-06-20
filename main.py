"""
PTT Drink 版爬蟲主執行檔案

直接爬取 Drink 版面
"""

import datetime
import os
from ptt_crawler import crawl_ptt_page


def main():
    """主要執行函數 - 只爬取 Drink 版"""
    print("=== PTT Drink 版爬蟲程式 ===")
    print("🚀 啟動 PTT 爬蟲")
    print("🎯 固定爬取版面: Drink")
    print()

    # 詢問要爬取的頁數
    try:
        page_input = input("請輸入要爬取的頁數 (直接按 Enter 爬取所有頁面): ").strip()
        if page_input:
            page_num = int(page_input)
            if page_num <= 0:
                print("頁數必須大於 0，改為爬取所有頁面")
                crawl_all = True
                page_num = None
            else:
                crawl_all = False
        else:
            # 預設爬取所有頁面
            crawl_all = True
            page_num = None
    except ValueError:
        print("輸入無效，改為爬取所有頁面")
        crawl_all = True
        page_num = None

    if crawl_all:
        print(f"\n📝 將爬取 Drink 版所有頁面")
        print("⚠️  這可能需要很長時間，請耐心等候")
    else:
        print(f"\n📝 將爬取 Drink 版 {page_num} 頁")
    print("=" * 50)

    try:
        # 直接開始爬蟲
        if crawl_all:
            data = crawl_ptt_page(Board_Name='Drink', crawl_all=True)
        else:
            data = crawl_ptt_page(Board_Name='Drink', page_num=page_num)

        if not data.empty:
            current_count = len(data)
            print(f"\n🎉 爬取完成！成功取得 {current_count} 筆資料")
        else:
            print("\n⚠️  未取得任何資料")
            print("📝 請檢查:")
            print("   - 網路連線是否正常")
            print("   - errors/ 目錄中的錯誤記錄")

    except KeyboardInterrupt:
        print(f"\n⚠️ 用戶中斷程式 (Ctrl+C)")
        print("程式已停止")

    except Exception as e:
        print(f"❌ 爬取時發生錯誤：{e}")

        # 記錄主程式錯誤
        error_log_file = f'errors/main_errors_{datetime.datetime.now().strftime("%Y%m%d")}.log'
        os.makedirs('errors', exist_ok=True)
        with open(error_log_file, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.datetime.now().isoformat()} - Error: {str(e)}\n")

    print("=" * 50)


if __name__ == "__main__":
    main()
