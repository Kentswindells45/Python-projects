def switch(lang):
    if lang == "javaScript":
        return "You become a web developer"
    elif lang == "PHP":
        return "You can become a backend developer"
    elif lang == "Python":
        return "You can become a data scientist"
    elif lang == "solidity":
        return "You can become a Blockchain developer"
    elif lang == "Java":
        return "You can become a mobile app developer"


print(switch("javaScript"))
print(switch("PHP"))
print(switch("Java"))
print(switch("Python"))
