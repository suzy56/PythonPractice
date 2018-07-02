# python 中的dict类似与js中的json数据
# dict 在python中的查询效率很高，类似与hashMap，key对应内存地址
# dict采用了哈希表，最低能在 O(1)时间内完成搜索。同样的java的HashMap也是采用了哈希表实现，
# 不同是dict在发生哈希冲突的时候采用了开放寻址法，而HashMap采用了链接法。

d = {'michael':98,'tom':88,'jack':87}

print(d['jack'])

print('tom' in d)

print(d.get('tom'))

print(d.get('bom'),-1)

d.pop('tom')

print(d)

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合

# 即使有重复元素也会过滤  set可以看成数学意义上的无序和无重复元素的集合

s = set([1,2,3,3,'jack','jack'])

print(s)