import multiprocessing

def square(n):
    """Returns the square of a number."""
    return n * n

if __name__ == "__main__":
    # รับค่าตัวเลขจากผู้ใช้
    user_input = input("Enter numbers separated by spaces: ")
    
    # แปลงเป็นลิสต์ของตัวเลข
    numbers = list(map(int, user_input.split()))

    # ใช้ multiprocessing เพื่อคำนวณกำลังสองแบบขนาน
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(square, numbers)

    print(f"Squares: {results}")
