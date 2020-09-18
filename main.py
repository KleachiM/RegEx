import  re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
for line in contacts_list:
  if len(line[0].split(' ')) == 3:
    for i in reversed(range(3)):
      line[i] = re.findall(r'\w+', line[0])[i]

  if len(line[0].split(' ')) == 2:
    for i in reversed(range(2)):
      line[i] = re.findall(r'\w+', line[0])[i]

  if len(line[1].split(' ')) == 2:
    for i in reversed(range(1,3)):
      line[i] = re.findall(r'\w+', line[1])[i-1]

  pattern = r'(\+7|8)\s*\(*(\d{3})\)*\s*-*(\d{3})-*(\d{2})-*(\d{2})($| \(?(доб\.) (\d+)\)?)'
  regex = re.compile(pattern)
  line[5] = regex.sub(r'+7(\2)\3-\4-\5 \7\8', line[5])

persons = []
contacts = []
for line in contacts_list:
    person = f'{line[0]} {line[1]}'
    if person not in persons:
      persons.append(person)
      contacts.append([])
      for i in range(7):
        contacts[persons.index(person)].append(line[i])
    else:
      for i in range(7):
        if contacts[persons.index(person)][i] == '':
          contacts[persons.index(person)][i] = line[i]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts)