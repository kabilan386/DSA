def test():
    try:
        return 10 / "a"
    except Exception as e:
        print(e)
        # return 2
    finally:
        print("finally")
    



test()