from roboflow import Roboflow
rf = Roboflow(api_key="ImxMauUX41hTySVncMrO")
project = rf.workspace("maximilian-sittinger").project("insect_detect_detection")
version = project.version(7)
dataset = version.download("yolov8")
