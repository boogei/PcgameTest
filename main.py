
تمارين لغة بايثون
مرحبًا، هذا الملف سيكون تقييمًا جيدًا لنا لمعرفة مهارتنا في لغة بايثون
من المهم لنا أن نتقن استخدام الأداة حتى نحقق أهدافنا، و أداتنا في هذا المعسكر هي لغة بايثون
سنطلب منك حل التحديات القصيرة أدناه، لتتمكن من تقييم نفسك ، بالتوفيق!

ملاحظة: لا يوجد حل واحد صحيح، و هذا ما يميز البرمجة حقًا

المهمة الأولى
لدينا أربعة متغيرات هنا، هل يمكننا برمجيًا معرفة نوع هذه المتغيرات؟
يرجى كتابة الحل المقترح

x = 7
y = x/3
z = x == 7
s = "Hello python programmer!"
type(x)
type(y)
type(z)
type(s)

المهمة الثانية
نرغب بطباعة الجملة التالية:
"I want to pay 10.5 riyals for 2 pieces of this item."
لكننا سنقوم باستخدام المتغيرات المعرفة لدينا (متغير السعر ومتغير الكمية) بدلا من إعادة كتابة الأرقام، هل يمكنك فعلها؟

quantity = 2
price = 10.5
text = "i want to pay {} for {} pieces for this item".format(quantity, price)
print(text)

المهمة الثالثة
قم بكتابة دالة تقوم بمقارنة الرقم المدخل (مثل ١٩) بالرقم ١٠ و تخبرك ما إذا كان أكبر من الرقم ١٠ أم لا

def bigger_than_10(x):
    if x > 10:
        print('bigger_than_10' + '(' + str(x) + ')')
    elif x < 10:
        print('smaller_than_10' + '(' + str(x) + ')')
    else:
        print('equal_to_10' + '(' + str(x) + ')')

bigger_than_10(19)

المهمة الرابعة
لدينا قائمة من الفواكه، كيف يمكننا برمجيا الحصول على آخر فاكهتين في القائمة؟

fruites = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruites[5], fruites[6]

هل يمكننا طباعة كل عنصر من القائمة السابقة في سطر مستقل؟

print ('\tapple\n', '\tbanana\n', '\tcherry\n', '\torange\n', '\tkiwi\n', '\tmelon\n', '\tmango\n')

المهمة الخامسة
لنفترض أن لدينا المعجم التالي، نريد إضافة المفتاح
black
بالقيمة
000000

colors = {
  "blue": "0000FF",
  "green": "00FF00",
  "yellow": "FFFF00",
  "red": "FF0000",
  "white": "unknown"
}

colors["black"] = "000000"

هل يمكننا تغيير قيمة المفتاح
white
بالقيمة
FFFFFF ?

colors["white"] = "FFFFFF"

نريد إنشاء دالة تقوم بأخذ قائمة و استبدال عناصرها بالقيم من المعجم بالاستعانة بالمفاتيح مثال: نستبدل
blue
بالقيمة
0000FF

def exchange_values(lista):
    lista[0] = colors['blue']
    lista[1] = colors['white']
    lista[2] = colors['black']
    lista[3] = colors['yellow']
    lista[4] = colors['green']
    lista[5] = colors['red']
    print(lista)

lista = ['blue', 'white', 'black', 'yellow', 'green', 'red']
exchange_values(lista)