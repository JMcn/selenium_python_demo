import os


def report_dir():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    report_path = path + "/report/image/"
    return report_path
