from dataclasses import dataclass

#file at the end we will get in artifacts folders

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

#file at the end we will get in artifacts folders
@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str