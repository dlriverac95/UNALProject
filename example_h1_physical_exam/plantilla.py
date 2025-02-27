
class console:
    def __init__(self):
        self.countInput = 0
        
    def getNumInput(self):
        res = self.countInput
        self.countInput += 1
        return res

def {{task_id}}_{{submition_id}}(var1):

    result = []
    consoleInput = console()
    def input(*args):
        return var1.split('~')[consoleInput.getNumInput()]
  
    ## 
    # codigo de la solución propuesta por el estudiante
    ##

    return result    


import unittest
class MyTestCase(unittest.TestCase):
    
    def test_{{name_case}}(self):
        {{name_case}} = {{task_id}}_{{submition_id}}("{{in}}")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in {{name_case}}]), "{{{{name_case}}.out}}")

    def test_{{name_case}}(self):
        {{name_case}} = {{task_id}}_{{submition_id}}("{{in}}")
        self.assertEqual(" ".join([str(x).replace("\n", " ") for x in {{name_case}}]), "{{{{name_case}}.out}}")