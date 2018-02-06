CAMEL_CASE_COUNT = 0;

def main():
    global CAMEL_CASE_COUNT
    listOfCsvFiles = collect_all_csv_filenames()
    read_csv_list(listOfCsvFiles)
    everyone = make_everyone_csv(listOfCsvFiles)
    write_csv(everyone)
    write_json(everyone)

    print("Camel case count is %d" %CAMEL_CASE_COUNT)


def collect_all_csv_filenames():
    from glob import glob
    listOfCsvFiles = []
    for filename in glob("*.csv"):
        if (filename != "mlp6.csv"):
            listOfCsvFiles.append(filename)

    return listOfCsvFiles



def read_csv_list(listOfCsvFiles):
    import pandas as pd
    teamNameIndex = 4;

    for file in listOfCsvFiles:
        reader = pd.read_csv(file, header = None)
        teamName = reader.values[0][teamNameIndex]
        check_no_spaces(teamName)
        check_camel_case(teamName)


def make_everyone_csv(listOfCsvFiles):
    import pandas as pd

    singleListOfCSV = []
    for file in listOfCsvFiles:


        singleListOfCSV.append(pd.read_csv(file, header = None).values[0])

    df = pd.DataFrame(singleListOfCSV)
    # print(df)
    return df

def write_csv(everyone):
    # print(everyone)
    everyone.to_csv("everyone.csv")


def write_json(everyone):
    import json
    netIDIndex = 2;
    for i in range(len(everyone)):
        netID = everyone.loc[i][netIDIndex]
        netIDwJSONExt = netID + ".json"
        personInfoList =[]
        for data in range(len(everyone.loc[i])):
            personInfoList.append(everyone.loc[i][data])
        with open(netIDwJSONExt,'w') as outfile:
            #print(personInfoList)
            json.dump(personInfoList, outfile)

# def write_json(everyone):
#     import json
#     import pandas
#     netIDIndex = 2;
#     for i in range(len(everyone)):
#         netID = everyone.loc[i][netIDIndex]
#         netIDwJSONExt = netID + ".json"
#         print(everyone.loc[i])
#         #everyone.loc[i].to_json(netIDwJSONExt)





def check_no_spaces(teamName):
    if (len(teamName.split())==0):
        print("There is a space in this TeamName, %s" %teamName)



def check_camel_case(teamName):
    global CAMEL_CASE_COUNT
    if (teamName.upper() != teamName and teamName.lower() != teamName):
        CAMEL_CASE_COUNT = CAMEL_CASE_COUNT + 1;


if __name__ == "__main__":
    main()
