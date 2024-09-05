from enum import IntEnum

class EHRDocCatEnum(IntEnum):
    OTHER = 0
    CONDITION_SUMMARY = 1
    EXAM = 2
    INSPECT = 3
    MEDICAL_RECORD = 4
    PRESCRIPTION = 5

    @property
    def lname(self):
        return self._name_.lower()
    

if __name__ == "__main__":
    archives_records_list = {category.lower_name: [] for category in EHRDocCatEnum}
    print(archives_records_list)
    print(EHRDocCatEnum.CONDITION_SUMMARY)
    print(EHRDocCatEnum.CONDITION_SUMMARY.value)
    print(EHRDocCatEnum.CONDITION_SUMMARY.name)
    
    