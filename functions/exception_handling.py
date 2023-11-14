

def find_file():
    try:
        with open("azam.txt", "r") as file:
            # Read and print the file contents
            file_contents = file.read()
            print("File contents:")
            print(file_contents)
            # time.sleep(5)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        file.close()  # Ensure the file is closed even if an exception occurs
        print("File is closed successfully.")
find_file()
