import sqlite3

conn = sqlite3.Connection('Youtube_videoes.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    # print(cursor)
    print("\n" + "*"*70)
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print("*"*70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def update_video(vid_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, vid_id))
    conn.commit()

def delete_video(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(vid_id, ))
    conn.commit()


def main():

    while True:
        print("\n Youtube Manager App With DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("enter your choice: ") 
        
        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        
        elif choice == '3':
            list_videos()
            video_id = int(input("Enter video Id to be Updated: ") )
            new_name = input("Enter video name: ")
            new_time = input("Enter video time: ")
            update_video(video_id, new_name, new_time)

        elif choice == '4':
            video_id = int(input("enter video Id: "))
            delete_video(video_id)

        elif choice == '5':
            break

    conn.close()

if __name__ == '__main__':
    main()