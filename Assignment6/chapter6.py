def main():
    method1()
        
def method1():
    while True:
        name = input("Enter your name: ")
        
        try:
            name = int(name)
            print("INVALID: Your name can only have letters in it")
            print()
        except ValueError:
            break  
        
    while True:   
        description = input("Tell us something about yourself, briefly: ")
            
        try:
           description = input(description)
           print("INVALID INPUT!")
           print()
        except IOError:
            break
          
    webCreator = open("Assignment6/webPage.html", "w")
    
    personal = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>%s</title>
        </head>
        <body>
        <h2>%s</h2>
        <p>Description: %s</p>
        </body>
        </html>
        """ % (name, name, description)  
        
    webCreator.write(personal)
    webCreator.close()
main()