

def main():
    names = []
    print('Exit in programing (stop)')
    while True:
        name = input("Enter your name: ")

        if name.lower() == 'stop':
            break

        names.append(name)

    return names

print('isimlar royxati\n',main())
