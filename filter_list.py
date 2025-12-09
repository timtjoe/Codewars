print("Hello world!")

def filter_list(l):
    'return a new list with the strings filtered out'
    filtered_list = [];
    for item in l:
      if not isinstance(item, str):
        filtered_list.append(item)
    return filtered_list

filter_list([1,2,'a','b']) 
# == [1,2]
filter_list([1,'a','b',0,15]) 
# == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) 
# == [1,2,123]