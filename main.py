from fgs.main import bind_messages

def main():
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")

    bind_messages()
    
    IvyMainLoop()

if __name__ == "__main__":
    main()