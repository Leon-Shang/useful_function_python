def short_print(num, name, *iter):
  names = name.split(',')
  for i, item in enumerate(iter):
    print(names[i]+'-'*(60-len(names[i])))
    for j, toshow in enumerate(item):
      if j == num:
        break
      try:
        if type(item) == dict:
          keys_list = list(item.keys())
          print(keys_list[j], ': ',item[keys_list[j]])
        else:
          print(toshow)
      except:
        print(item)
        break
