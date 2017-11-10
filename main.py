from untagged.representer import vectorSpaceModel


def main(): 
    string = "abc a b c d e f"
    string2 = "osdj slajd slkj"
    #vectorSpaceModel.inverted_file(string, 10)
    vectorSpaceModel.inverted_file(string2, 20)
    


if __name__ == "__main__":
    main()
