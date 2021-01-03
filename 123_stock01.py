import pandas_datareader.data as web  # ไลบรารีที่เราจะใช้ดึงข้อมูลหุ้น
import datetime as dt  # ไลบรารีที่เราจะใช้สำหรับงานที่เกี่ยวข้องกับ วันเวลา
import pandas as pd  # ไลบรารีที่เราจะใช้ทำงานเกี่ยวกับตาราง (Dataframe)

stock_name = "SCB.BK"  # ใส่ชื่อของหุ้นที่เราจะดึงข้อมูล ในที่นี้คือ SCB
start_date = dt.date(2016, 9, 1)  # กำหนดวันแรกที่จะดึงข้อมูล
end_date = dt.date(2019, 8, 30)  # กำหนดวันสุดท้ายที่จะดึงข้อมูล
# ดึงข้อมูลมาเก็บไว้ในตัวแปร df
df = web.get_data_yahoo(stock_name, start_date, end_date)
df.to_csv("SCB.csv")  # save ข้อมูลหุ้นเก็บไว้เป็นไฟล์ .csv

stock = df.head(100)
print(stock)
