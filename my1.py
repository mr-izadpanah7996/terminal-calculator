import os
import shutil

def ali():
    try:
        file_format = input("فرمت فایلها رو وارد کن (مثلا mp3, txt, py): ").strip().lower()
        source = input("آدرس مبدع رو وارد کن: ").strip()
        destination = input("آدرس مقصد رو وارد کن: ").strip()

        source = os.path.normpath(os.path.expanduser(source))
        destination = os.path.normpath(os.path.expanduser(destination))

        if not os.path.exists(source):
            raise FileNotFoundError(f"❌ آدرس مبدع وجود ندارد: {source}")
        if not os.path.isdir(source):
            raise NotADirectoryError(f"❌ آدرس مبدع یک پوشه نیست: {source}")

        if not os.path.exists(destination):
            try:
                os.makedirs(destination, exist_ok=True)
            except Exception as e:
                raise PermissionError(f"❌ ساخت پوشه مقصد ممکن نیست: {destination} -> {e}")
        if not os.path.isdir(destination):
            raise NotADirectoryError(f"❌ آدرس مقصد یک پوشه نیست: {destination}")

        files = os.listdir(source)
        if not files:
            raise FileNotFoundError("❌ پوشه مبدع خالی است.")

        matched_files = [
            f for f in files
            if os.path.isfile(os.path.join(source, f)) and os.path.splitext(f)[1].lower() == f".{file_format}"
        ]
        if not matched_files:
            raise FileNotFoundError(f"❌ هیچ فایلی با فرمت .{file_format} در مسیر مبدع یافت نشد: {source}")

        moved_count = 0
        for f in matched_files:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            try:
                shutil.move(src_path, dst_path)
                moved_count += 1
                
            except Exception as e:
                print(f"⚠️ انتقال {f} شکست خورد: {e}")

        print(f"\n✅ تعداد {moved_count} فایل با فرمت .{file_format} منتقل شد.")
    except Exception as e:
        print(e)


ali()