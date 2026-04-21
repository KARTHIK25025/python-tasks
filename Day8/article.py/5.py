with open("article.txt", "w") as file:
    file.write("Python is easy.\nIt is powerful.")
def analyze_article():
    try:
        with open("article.txt", "r") as file:
            content = file.read()
 
            characters = len(content)
 
            words = len(content.split())
 
            lines = len(content.splitlines())
 
            print("Number of characters:", characters)
            print("Number of words:", words)
            print("Number of lines:", lines)
 
    except FileNotFoundError:
        print("article.txt file not found.")
 
analyze_article()
