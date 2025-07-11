file_name = 'youtube.txt'
import json

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duartion: {video['time']}")
    print('*' * 70)

def add_videos(videos):
    name = input("Enter Video name: ")
    time = input("Enter Video Time: ")
    videos.append({'name': name, 'time': time})

    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter The video no. to Delete:"))

    if 1 <= index <= len(videos):
        name = input("enter the new Video name: ")
        time = input("enter the new Video time: ")

        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Item")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter The video no. to be Deleted:"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index no. selected")


def main():
    videos =load_data()
    
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. list all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos Detail")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        # print(videos)
    
        choice = input("Enter Your choice: ")
    
        # if choice == '1':
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
    
if  __name__ == "__main__":
    main()