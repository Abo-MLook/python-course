

def hello(name , lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",

    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == "__main__" :
    import argparse

    parser = argparse.ArgumentParser(
        description  = "provide a personal greeting."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True , help = "The name of perosn"
    )

    parser.add_argument(
        "-l","--lang",metavar="language"
        ,required= True , choices= ["English", "Spanish", "German"]
        , help = "The language of the greeting"
    )

    args = parser.parse_args()

    hello(args.name,args.lang)


    # in command line:
    #  py hello_person.py -n Ali -l English