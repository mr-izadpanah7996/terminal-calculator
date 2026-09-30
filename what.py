import os

file_name = "phonbook.txt"

def ad():
	try:
		name = input("اسم مخاطبی که میخوای رو وارد کن. ")
		number = int(input("شماره تلفن مخاطبی که میخوای اضافه کنی رو وارد کن. "))
		
		with open(file_name, "a", encoding="utf-8") as file:
		
			file.write(f"{name}, {number}\n")
		
		print("مخاطب افضوده شد. ")
		
	except:
		print("خطا در افضودن مخاطب! ")
		
		
def search():
	try:
		name = input("اسم مخاطب را برای جستجو وارد کنید. ")
		
		found = False
		
		with open(file_name, "r", encoding="utf-8") as file:
		
			for line in file:
				if name in line:
					print("مخاطب پیدا شد. ", line.strip())
					found = True
					break
				
		if not found:
			print("مخاطب پیدا نشد!! ")
			
	except:
		print("خطا در پیدا کردن مخاطب! ")
		

def delete():
	try:
		name = input("اسم مخاطب رو برای حضف وارد کن. ")
		found = False
		new_lines = []
		
		with open(file_name, "r", encoding="utf-8") as file:
		
			for line in file:
				if name not in line:
					new_lines.append(line)
				
				else:
					found = True
				
					with open(file_name, "w", encoding="utf-8") as file:
				
						file.writelines(new_lines)
				
		if found:
			print("مخاطب حضف شد. ")
			
		else:
			print("مخاطب حضف نشد!!! ")
			
	except:
		print("خطا در حضف مخاطب!! ")
		
		
def show_all():
	try:
		if not os.path.exists(file_name):
			print("فایل هنوز ساخته نشده. ")

			return


		with open(file_name, "r", encoding="utf-8") as file:
		
			lines = file.readlines()
		
		if not lines:
			print("لیست مخاطبین خالی هستش!! ")
			return

		print("لیست مخاطبین. ")
			
		for line in lines:
			name, number = line.strip().split(",")
				
			print("نام", name, "شماره", number)
				
	except:
		print("خطا در نمایش مخاطبین!! ")
		
		
def run():
	while True:
		try:

			print("یک افضودن مخاطب. ")
			print("دو جستجو مخاطب. ")
			print("سه حضف مخاطب. ")
			print("چهار نمایش لیست همه مخاطبین. ")
			print("پنج خروج از برنامه. ")
		
			choice = int(input("انتخاب شما؟؟؟ "))
		
			if choice == 1:
				ad()
			elif choice == 2:
				search()
			elif choice == 3:
				delete()
			elif choice == 4:
				show_all()
			elif choice == 5:
				print("از برنامه خارج شدی!! خدانگهدار. ")
				break
			else:
				print("انتخاب نامعتبر است!!! ")
			
		except ValueError:
			print("لطفا فقط عدد وارد کنید. ")

run()