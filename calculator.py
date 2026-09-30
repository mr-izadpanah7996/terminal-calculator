# Terminal Calculator Version 1.1

def jam():

    try:
        x = 0

        print("عملیات جمع عددهات رو یکی یکی وارد کن و اینتر بزن \n")
        print("برای جمع زدن آخر سر کلمه تمام رو به فارسی بنویس و اینتر بزن \n")

        while True:
            number = input("عددت رو وارد کن. ")

            if number == "تمام":
                print("نتیجه جمع کل میشود", x)
                break

            adad = int(number)

            x += adad

            print("نتیجه جمع تا اینجا", x)

    except ValueError:

        print("خطا!! لطفا یا عدد وارد کن یا بنویس تمام. ")


def tafreq():

    try:
        x = None

        print("عملیات تفریق یکی یکی عددهات رو وارد کن و اینتر بزن \n")
        print("برای دیدن نتیجه نهایی یعنی همون مساوی زدن به فارسی بنویس تمام \n")

        while True:
            number = input("عددت رو وارد کن. ")

            if number == "تمام":
                print("نتیجه نهایی است", x)
                break

            adad = int(number)

            if x is None:

                x = adad

            else:

                x -= adad

                print("نتیجه تا به اینجا است", x)

    except ValueError:
        print("خطا لطفا یا عدد وارد کن یا بنویس به فارسی تمام. ")


def zarbe():

    try:

        print("عملیات ضرب. ")
        print("عدد ها رو یکی یکی وارد کن و اینتر بزن \n")
        print("برای دیدن نتیجه مساوی کلمه ی تمام رو به فارسی بنویس \n")

        x = None

        while True:

            number = input("عددت رو وارد کن. ")

            if number == "تمام":
                print("نتیجه نهایی است", x)
                break

            adad = int(number)

            if x is None:
                x = adad

            else:

                x *= adad
                print("نتیجه تا به اینجا", x)

    except ValueError:

        print("خطا لطفا فقط یا عدد وارد کن یا بنویس به فارسی تمام. ")


def tagsim():

    try:

        print("عملیات تقسیم \n")
        print("یکی یکی عدد هات رو وارد کن و اینتر بزن \n")
        print("برای دیدن نتیجه نهایی کلمه تمام رو به فارسی بنویس \n")

        x = None

        while True:

            number = input("عددت رو وارد کن. ")

            if number == "تمام":
                print("نتیجه نهایی است", x)
                break

            adad = int(number)

            if adad == 0 and x is not None:
                print("ارور تقسیم بر صفر مجاز نیست. ")
                continue

            if x is None:
                x = adad

            else:
                x /= adad
                print("نتیجه تا به اینجا", x)

    except ValueError:
        print("خطا لطفا فقط عدد وارد کن یا به فارسی بنویس تمام. ")


def tavan():

    try:
        print("عملیات توان \n")

        base = int(input("عدد بیس رو وارد کن. "))
        power = int(input("عدد توانش رو وارد کن. "))

        result = base**power

        print(f"عدد {base} به توان {power} میشود {result}")

    except ValueError:
        print("خطا لطفا فقط عدد وارد کنید. ")


def main():
    while True:
        try:
            print("برنامه ماشین حساب. ")
            print("یک عملیات جمع. ")
            print("دو عملیات تفریق. ")
            print("سه عملیات ضرب. ")
            print("چاهار عملیات تقسیم. ")
            print("پنج عملیات توان. ")
            print("شش خروج از برنامه. ")

            choice = int(input("انتخاب شما؟؟ "))

            if choice == 1:
                jam()

            elif choice == 2:
                tafreq()

            elif choice == 3:
                zarbe()

            elif choice == 4:
                tagsim()

            elif choice == 5:
                tavan()

            elif choice == 6:
                print("از برنامه خارج شدی. ")
                break

            else:
                print("انتخاب نامعتبر لطفا از بین عددهای یک تا شش یکی رو انتخاب کن. ")

        except ValueError:
            print("خطا نامشخص ")


main()
