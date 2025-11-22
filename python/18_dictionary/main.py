dict = {
    "name": "meet desai",
    "cgpa": 7.1,
    "subjects": ["math", "science"],
    3.14: "PI"
}

print(dict)
print(dict["name"])
print(dict["cgpa"])
dict["subjects"] = ["guj", "eng"]

# methods

print(dict.keys())
print(dict.values())
print(dict.get(3.14))
print(dict.update({"city": "surat"}))


print(dict)
