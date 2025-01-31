from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
import bson
import os

# Declarando valores
DB_URL = "mongodb://localhost:27017"
DB_USERNAME = "<empty>"
DB_PASSWORD = "<empty>"
DB_NAME = "INGInious"

script_dir = os.path.dirname(__file__)

client = MongoClient(DB_URL)

uncode_backup_db = client[DB_NAME]
fs_submissions_col = uncode_backup_db["submissions"]
fs = gridfs.GridFS(uncode_backup_db)

# Commented out IPython magic to ensure Python compatibility.
# Create folder
os.getcwd()

# Ruta de la base de datos
path = 'D:\\Uniandes\\Semana4\\MonkeyWeb\\cypress\\e2e'

#Crear carpeta en mi pc
s = 'Learning-Analytics'

def main():
    cursor = fs_submissions_col.aggregate([{"$match": {"courseid" : 'IALPCP-GroupMLDS-2021-2', "result" : "success"}}])
    for submition in list(cursor):
        input = submition["input"]
        courseId = submition["courseid"]
        taskId = submition["taskid"]
        username = str.join('_',submition["username"]).replace(".", "_")
        id : ObjectId = submition["_id"]
        dataFile = fs.get(input)
        bson_dict = bson.BSON.decode(dataFile.read())
        l = [key for key in bson_dict.keys() if '/' not in key and '@' not in key]
        try:
            tempdir = os.path.join(script_dir, "extractfile" , courseId, taskId)
            fileName = "{}-{}-{}.py".format(username, taskId, id.__str__())
            if not os.path.exists(tempdir):
                os.makedirs(tempdir)
    
            tempdir = os.path.join(tempdir, fileName)
            with open(tempdir, "x", encoding="utf-8") as file:
                binary_data = bson_dict[l[0]]
                file.write(binary_data)
            buildFile(tempdir, taskId, courseId, id, username)  
        except Exception as e:
            print("{}-{}".format(taskId, username))
            print(e)
            #print(binary_data)
            raise

def buildFile(fileName: str, taskId: str, courseId: str, id: ObjectId, username: str):
    tempdir = os.path.join(script_dir, "extractfile", "buildfile" , courseId, taskId)
    fileNameBuild = "test_{}-{}-{}.py".format(username, taskId, id.__str__())
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    
    fw = open(os.path.join(tempdir, fileNameBuild), "x", encoding = "utf-8")
      
    # Write file
    rebuildFile = buildFileMain(fileName, taskId, courseId, id, username)
    fw.write("\n".join(rebuildFile)) 
       
     # Write file test
    rebuildFileTest = buildFileTest(taskId, id)
    fw.write("\n".join(rebuildFileTest))
    fw.close()

def buildFileMain(fileName : str, taskId : str, courseId : str, id: ObjectId, username: str):
    fExerciseOri = open(fileName, encoding="utf-8")
    lines = fExerciseOri.readlines()
    fExerciseOri.close()
    
    countReturns = len(find_all(str.join("\n", lines), "print"))
    rebuildFile = []
    variableMethod = []

    variableMethod.append("var1")

    rebuildFile.append("""
class console:
    def __init__(self):
        self.countInput = 0
        
    def getNumInput(self):
        res = self.countInput
        self.countInput += 1
        return res""")
    
    rebuildFile.append("def {}{}({}):\n".format(taskId, id.__str__(), str.join(",", variableMethod)))
    rebuildFile.append("{}result = []".format(addspace(1)))
    rebuildFile.append("{}consoleInput = console()".format(addspace(1)))

    #Get inputs
    rebuildFile.append("{}def input(*args):".format(addspace(1)))
    rebuildFile.append("{}return var1.split('~')[consoleInput.getNumInput()]".format(addspace(2)))

    mainDef = False

    # Finish build file
    for line in lines:
        if line.__contains__("main()"):
            mainDef = True
            if not line.__contains__("def"):
                rebuildFile.append("{}".format(line))
        elif line.__contains__("print"):
            if mainDef:
                rebuildFile.append("{}".format(line.replace("print", "result.append")))
            else:
                rebuildFile.append("{}{}".format(addspace(1), line.replace("print", "result.append")))
            countReturns -= 1
            if countReturns == 0:
                rebuildFile.append("{}{}".format(addspace(1), "return result"))
        else:
            if mainDef:
                rebuildFile.append("{}".format(line))
            else:
                rebuildFile.append("{}{}".format(addspace(1), line))
    return rebuildFile

def buildFileTest(taskId: str, id: ObjectId):
    rebuildFileTest = []

    # Init write test
    rebuildFileTest.append("""
import unittest
class MyTestCase(unittest.TestCase):
    """)
            
    pathTC = os.path.join(script_dir, 'answers/{}'.format(taskId))
    dirAnwsers = os.listdir(pathTC)
    for file in dirAnwsers:
        if file.endswith(".in"):
            fileNameTest = file.split(".in")[0]
            fin = open(os.path.join(pathTC, file), encoding="utf-8")
            fout = open(os.path.join(pathTC, fileNameTest + ".out"), encoding="utf-8")
            rebuildFileTest.append("{}def test_{}(self):".format(addspace(1), fileNameTest))
            inResult = []
            for line in fin.readlines():
                if line.strip() == "":
                    continue
                inResult.append(line.strip())

            if fileNameTest.isnumeric():
                fileNameTest = "{}{}".format("a", fileNameTest)
        
            rebuildFileTest.append("{}{} = {}{}(\"{}\")".format(addspace(2), fileNameTest, taskId, id.__str__(), str.join("~", inResult)))

            outResult = []
            for line in fout.readlines():
                if line.strip() == "":
                    continue
                outResult.append(line.strip())
                
            rebuildFileTest.append("{}self.assertEqual(\" \".join([str(x).replace(\"\\n\", \" \") for x in {}]), \"{}\")".format(addspace(2), fileNameTest, " ".join(outResult)))

        fout.close()
        fin.close()

    return rebuildFileTest           
            
def addspace(level):
    return " " * level * 4

def find_all(a_str, sub):
    start = 0
    matches = []
    while True:
        start = a_str.find(sub, start)
        if start == -1: return matches
        matches.append(start)
        start += len(sub) # use start += 1 to find overlapping matches

main()