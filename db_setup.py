import MySQLdb

# 接続開始
conn = MySQLdb.connect(
    user='root',
    password='',
    host='localhost',
    db='mysql',
    charset='utf8'
)
cur = conn.cursor()

# データベースの作成
cur.execute('drop database if exists rabbitexpress')
cur.execute('create database rabbitexpress default character set utf8')
print('DBを作成しました')
cur.execute('use rabbitexpress')
print('作成したDBを使用します')

# テーブルの作成
# users
cur.execute('drop table if exists users')
sql = '''
    create table users (
        id int not null auto_increment primary key,
        name varchar(255) not null,
        email varchar(255) not null,
        password varchar(255) not null)'''
cur.execute(sql)
print('usersテーブルを作成しました')
# items
cur.execute('drop table if exists items')
sql = '''
    create table items (
        id int not null auto_increment primary key,
        name varchar(255) not null,
        text text,
        price int not null,
        stock int not null,
        img1 text,
        img2 text,
        img3 text)'''
cur.execute(sql)
print('itemsテーブルを作成しました')
# order
cur.execute('drop table if exists orders')
sql = '''
    create table orders (
        id int not null auto_increment primary key,
        users_id int not null,
        items_num int not null,
        created datetime not null)'''
cur.execute(sql)
print('ordersテーブルを作成しました')
# orders_detail
cur.execute('drop table if exists orders_detail')
sql = '''
    create table orders_detail (
        orders_id int not null,
        items_id int not null,
        purchase_num int not null)'''
cur.execute(sql)
print('orders_detailテーブルを作成しました')

# テーブル一覧の取得
print('テーブル一覧を表示します')
cur.execute('show tables')
for row in cur:
    print(row)


# データの追加
print('テーブルにデータを追加します')
# users
sql = '''
    insert into users(
        name,
        email,
        password
    ) values (
        "佐藤太郎",
        "tarosato@dummy.com",
        "satotaro0123"
    ),(
        "鈴木一郎",
        "suzuki_ichiro@dummy.com",
        "suzuki_1ro"
    ),(
        "高橋修二",
        "takasyu312@dummy.com",
        "takataka312"
    )'''
cur.execute(sql)
print('usersデータを追加しました')
# items
sql = '''
    insert into items(
        name,
        text,
        price,
        stock,
        img1,
        img2,
        img3
    ) values (
        "りんご",
        "長野県産のサンふじ",
        250,
        300,
        "apple_img1.png",
        "apple_img2.png",
        ""
    ),(
        "ぶどう",
        "岡山県産のピオーネ",
        1980,
        30,
        "grape_img1.png",
        "grape_img2.png",
        ""
    ),(
        "みかん",
        "愛媛県産の温州みかん",
        30,
        3000,
        "mikan_img1.png",
        "mikan_img2.png",
        "mikan_img3.png"
    ),(
        "グレープフルーツ",
        "南アフリカ産のルビー",
        180,
        120,
        "grapefruit_img1.png",
        "grapefruit_img2.png",
        "grapefruit_img3.png"
    ),(
        "いちご",
        "福岡県産のあまおう",
        150,
        500,
        "ichigo_img1.png",
        "ichigo_img2.png",
        ""
    ),(
        "レモン",
        "瀬戸内産のレモン",
        98,
        800,
        "lemon_img1.png",
        "lemon_img2.png",
        ""
    ),(
        "スイカ",
        "熊本県産のスイカ",
        3800,
        20,
        "suika_img1.png",
        "suika_img2.png",
        ""
    ),(
        "さくらんぼ",
        "山形県産の佐藤錦",
        100,
        1000,
        "cherry_img1.png",
        "",
        ""
    ),(	
        "ライム",
        "岡山県産のライム",
        88,
        900,
        "lime_img1.png",
        "lime_img2.png",
        ""
    ),(
        "アセロラ",
        "沖縄県石垣島産のアセロラ",
        20,
        1200,
        "acerola_img1.jpg",
        "",
        ""
    ),(	
        "柿",
        "和歌山県産の種なし柿",
        120,
        90,
        "kaki_img1.png",
        "",
        ""
    ),(	
        "桃",
        "山形県産の白桃",
        700,
        70,
        "peach_img1.png",
        "",
        ""
    ),(	
        "メロン",
        "静岡県産のクラウンメロン",
        6500,
        35,
        "melon_img1.png",
        "",
        ""
    ),(	
        "プルーン",
        "カリフォルニア産のプルーン",
        10,
        3200,
        "prune_img1.png",
        "",
        ""
    ),(	
        "パイナップル",
        "沖縄県産のパイナップル",
        2000,
        80,
        "pineapple_img1.png",
        "",
        ""
    ),(	
        "梨",
        "鳥取県産の王秋",
        400,
        150,
        "pear_img1.png",
        "",
        ""
    )'''
cur.execute(sql)
print('itemsデータを追加しました')
# orders
sql = '''
    insert into orders(
        users_id,
        items_num,
        created
    ) values (
        1,
        2,
        "2020/10/12 11:54:36"
    ),(
        3,
        1,
        "2020/10/14 10:05:07"
    ),(
        1,
        3,
        "2020/10/16 14:54:38"
    )'''
cur.execute(sql)
print('ordersデータを追加しました')
# orders_detail
sql = '''
    insert into orders_detail(
        orders_id,
        items_id,
        purchase_num
    ) values (
        1,
        1,
        20
    ),(
        1,
        3,
        50
    ),(
        2,
        2,
        2
    ),(
        3,
        1,
        20
    ),(
        3,
        2,
        7
    ),(
        3,
        3,
        50
    )
    '''
cur.execute(sql)
print('orders_detailデータを追加しました')


# 保存
conn.commit()

# 接続終了
conn.close()