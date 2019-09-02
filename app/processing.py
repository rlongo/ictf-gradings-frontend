#!/bin/python3

import argparse
import os
import zipfile

from ictf_pipeline.parsers import StudentIteratorExcel, BeltLookupXML, PaperworkJPEGForm
from ictf_pipeline.aggregators import BeltOrderAggregator, RegistrationListAggregator
from ictf_pipeline import ictfpl

aggregators = [BeltOrderAggregator(), RegistrationListAggregator()]

forms = dict()

belt_lookup = BeltLookupXML("app/inputs/belts.xml")

# Get all forms
for file in os.listdir("app/inputs/forms"):
    if file.endswith(".xml"):
        name = file.split('.')[0]
        form = os.path.join("app/inputs/forms", file)
        forms[name] = PaperworkJPEGForm(name, form[:-4], form)


def compress_output(outdir):
    f = os.path.join(outdir, 'ICTF_TestData.zip')
    zipf = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    pwd = os.getcwd()
    try:
        os.chdir(os.path.join(outdir, 'GOOD'))

        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                zipf.write(file)
    except BaseException:
        raise
    finally:
        os.chdir(pwd)
        zipf.close()

    return f


def run_pipeline(outdir, students_io, config):
    student_iter = StudentIteratorExcel(students_io, belt_lookup)
    ictfpl(forms, aggregators, student_iter, outdir, config)
    return compress_output(outdir)
