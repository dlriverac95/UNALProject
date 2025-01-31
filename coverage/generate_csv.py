import os
import json
from typing import Dict
from dataclasses import field
import pandas as pd
from pydantic import BaseModel

class Meta():
    def __init__(self, format, version, timestamp, branch_coverage, show_contexts):
        self.format = format
        self.version = version
        self.timestamp = timestamp
        self.branch_coverage = branch_coverage
        self.show_contexts = show_contexts

class Totals():
    def __init__(self, covered_lines, num_statements, percent_covered, percent_covered_display, missing_lines, excluded_lines,
                 num_branches, num_partial_branches, covered_branches, missing_branches):
        self.covered_lines = covered_lines
        self.num_statements = num_statements
        self.percent_covered = percent_covered
        self.percent_covered_display = percent_covered_display
        self.missing_lines = missing_lines
        self.excluded_lines = excluded_lines
        self.num_branches = num_branches
        self.num_partial_branches = num_partial_branches
        self.covered_branches = covered_branches
        self.missing_branches = missing_branches

class Summary():
    def __init__(self, covered_lines, num_statements, percent_covered, percent_covered_display, missing_lines, excluded_lines, 
                 num_branches, num_partial_branches, covered_branches, missing_branches):
        self.covered_lines = covered_lines
        self.num_statements = num_statements
        self.percent_covered = percent_covered
        self.percent_covered_display = percent_covered_display
        self.missing_lines = missing_lines
        self.excluded_lines = excluded_lines
        self.num_branches = num_branches
        self.num_partial_branches = num_partial_branches
        self.covered_branches = covered_branches
        self.missing_branches = missing_branches
        
class File():
    def __init__(self, summary: Summary, missing_lines: list, 
                 excluded_lines: list, executed_branches: list, missing_branches: list):
        #self.executed_lines = executed_lines
        self.summary = summary
        #self.missing_lines =missing_lines
        #self.excluded_lines =excluded_lines
        #self.executed_branches =executed_branches
        #self.missing_branches =missing_branches

class Files():
    mapa: Dict[str, File] = field(default_factory=dict)
    def __init__(self, mapa) -> None:
        self.mapa = mapa

class Coverage():
    def __init__(self, meta: Meta, files: Files, totals: Totals) -> None:
        self.meta = meta
        self.files = files
        self.totals = totals

class CSV:
    def __init__(self, name_file, course_id, covered_lines, num_statements, percent_covered, percent_covered_display, missing_lines, excluded_lines, 
                num_branches, num_partial_branches, covered_branches, missing_branches):
        self.name_file = name_file
        self.course_id = course_id
        self.covered_lines = covered_lines
        self.num_statements = num_statements
        self.percent_covered = percent_covered
        self.percent_covered_display = percent_covered_display
        self.missing_lines = missing_lines
        self.excluded_lines = excluded_lines
        self.num_branches = num_branches
        self.num_partial_branches = num_partial_branches
        self.covered_branches = covered_branches
        self.missing_branches = missing_branches

    def to_dict(self):
        return {
            'name_file': self.name_file,
            'course_id': self.course_id,
            'covered_lines': self.covered_lines,
            'num_statements': self.num_statements,
            'percent_covered': self.percent_covered,
            'percent_covered_display': self.percent_covered_display,
            'missing_lines': self.missing_lines,
            'excluded_lines': self.excluded_lines,
            'num_branches': self.num_branches,
            'num_partial_branches': self.num_partial_branches,
            'covered_branches': self.covered_branches,
            'missing_branches': self.missing_branches,
        }

class CSVSummary:
    def __init__(self, name_file, covered_lines, num_statements, percent_covered, percent_covered_display, missing_lines, excluded_lines, 
                num_branches, num_partial_branches, covered_branches, missing_branches, submitTask):
        self.name_file = name_file
        self.covered_lines = covered_lines
        self.num_statements = num_statements
        self.percent_covered = percent_covered
        self.percent_covered_display = percent_covered_display
        self.missing_lines = missing_lines
        self.excluded_lines = excluded_lines
        self.num_branches = num_branches
        self.num_partial_branches = num_partial_branches
        self.covered_branches = covered_branches
        self.missing_branches = missing_branches
        self.submitTask = submitTask

    def to_dict(self):
        return {
            'name_file': self.name_file,
            'covered_lines': self.covered_lines,
            'num_statements': self.num_statements,
            'percent_covered': self.percent_covered,
            'percent_covered_display': self.percent_covered_display,
            'missing_lines': self.missing_lines,
            'excluded_lines': self.excluded_lines,
            'num_branches': self.num_branches,
            'num_partial_branches': self.num_partial_branches,
            'covered_branches': self.covered_branches,
            'missing_branches': self.missing_branches,
            'submit_task': self.submitTask
        }

script_dir = os.path.dirname(__file__)
files = [f for f in os.listdir(script_dir) if os.path.isfile(os.path.join(script_dir, f))]
fileCSVAll = []
fileSummaryExercise = []
for file in files:
    fileCoverage = os.path.join(script_dir, file)
    _, extension = os.path.splitext(file)
    if extension.lower() != '.json':
        continue

    with open(fileCoverage, encoding="utf-8") as fileCove:
        fileDataComplete: str = str.join("" ,fileCove.readlines())
        jsonData = json.loads(fileDataComplete)

    coverageFile = Coverage(**jsonData)

    rowSummaryCSV = CSVSummary(file.replace("coverage_", "").replace(".json", ""), 
                               coverageFile.totals["covered_lines"], coverageFile.totals["num_statements"], coverageFile.totals["percent_covered"], 
                               coverageFile.totals["percent_covered_display"], coverageFile.totals["missing_lines"], coverageFile.totals["excluded_lines"], 
                               coverageFile.totals["num_branches"], coverageFile.totals["num_partial_branches"], coverageFile.totals["covered_branches"], 
                               coverageFile.totals["missing_branches"], len(coverageFile.files))

    fileSummaryExercise.append(rowSummaryCSV)

    if "total" in file:
        continue

    for nameFile in coverageFile.files:
        fileData = coverageFile.files[nameFile]["summary"]

        lenPath = nameFile.split("\\")
        nameFileSplit = lenPath[len(lenPath)-1]
        courseId = nameFileSplit.split("-")[len(nameFileSplit.split("-"))-2]

        rowCSV = CSV(nameFile, courseId, fileData["covered_lines"], fileData["num_statements"], 
                fileData["percent_covered"], fileData["percent_covered_display"], 
                fileData["missing_lines"], fileData["excluded_lines"], 
                fileData["num_branches"], fileData["num_partial_branches"],
                fileData["covered_branches"], fileData["missing_branches"])
        
        fileCSVAll.append(rowCSV)

df = pd.DataFrame(json.loads(json.dumps([csv.to_dict() for csv in fileCSVAll])))
df.to_csv('file.csv', index=False)

dfSummaryExercise = pd.DataFrame(json.loads(json.dumps([csv.to_dict() for csv in fileSummaryExercise])))
dfSummaryExercise.to_csv('fileSummaryExercise.csv', index=False)