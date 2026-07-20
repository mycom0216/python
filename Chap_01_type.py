#dictionary 
dict1 = {"하나": 1, 
        "둘": 2, 
        "셋": 3}
print(dict1)

print(dict1["하나"])
dict1["추가"] = "값"
dict1["하나"] = 100

dict1.pop("하나")
dict1.update({"새키": "새값", "또키": 2})
print(dict1)

print(dict1.keys())
dict1 = {1: "하나", 2: "둘"} 
dict1_keys = list(dict1.keys())
print(dict1_keys)