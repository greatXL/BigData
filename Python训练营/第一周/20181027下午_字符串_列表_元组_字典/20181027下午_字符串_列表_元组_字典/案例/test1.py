s1 = "how are you doing?"
s2 = "HOW ARE YOU DOING?"
print(len(s1))#返回字符串s的长度
print(s1.upper())
print(s2.lower())
print(s1.index("how"))#返回“how”在s1中第一次出现的位置
print(s1.find("how"))#返回“how”在s1中第一次出现的位置
print(s1.find("z"))#没有出现，返回-1
print(s1.startswith("how"))#判断s1是否是以how开头
print(s1.endswith("?"))#判断s1是否是以？结尾
print(s1.count("o"))#返回o在s1中出现的次数
s3 = "   ab  "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())
print(s1.replace("o","O"))#将s1中所有的o替换成O
