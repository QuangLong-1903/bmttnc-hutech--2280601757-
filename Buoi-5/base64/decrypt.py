import base64

def main():
    try:
        with open("data.txt","r")as file:
            encode_string = file.read().strip()
        decoded_bytes = base64.b64decode(encode_string)
        decoded_string = decoded_bytes.decode("utf-8")
        print("Chuỗi sau khi giải mã:",decoded_string)
    except Exception as e:
        print("Lỗi rồi",e)
if __name__=="__main__":
    main()