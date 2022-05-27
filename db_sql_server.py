import pymssql
def db():
    conn=pymssql.connect(
        host="STAPDB01",
        user="portal",
        password="apportal",
        database="AutoPricing"
        )
    if conn:
        print("connected")
    return conn



if __name__ == "__main__":
    conn = db()
    # cursor= conn.cursor(as_dict=True)
    # sql="select top 10 * from dbo.priceinfo"
    # cursor.execute(sql)
    # data=cursor.fetchall()
    # print(data)
    # conn.commit()
    # cursor.close()


    