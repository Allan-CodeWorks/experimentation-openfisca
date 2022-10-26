from typing import List


class BenefitCondition():
    type = str
    values = list
    operator = str

    def __init__(self, dict: dict) -> None:
        self.type = dict.get('type', '')
        self.values = dict.get('values', [])
        self.operator = dict.get('operator', '')


class BenefitProfile():
    type: str
    conditions: list

    def __init__(self, dict: dict) -> None:
        self.type = dict.get('type', '')
        self.conditions = [BenefitCondition(
            condition) for condition in dict.get('conditions', [])]


class Benefit():
    label = str
    institution = str
    description = str
    prefix = str
    conditions_generales: list
    profils: List[BenefitProfile]
    conditions: list
    interestFlag: str
    type: str
    unit: str
    periodicite: str
    montant: int
    link: str
    instructions: str
    teleservice: str
    periodicite: str
    legend: str

    def __init__(self, dict: dict) -> None:

        try:
            self.label = dict.get('label', '')
            self.institution = dict.get('institution', '')
            self.description = dict.get('description', '')
            self.prefix = dict.get('prefix', '')
            self.conditions_generales = [BenefitCondition(
                condition) for condition in dict.get('conditions_generales', [])]
            self.profils = [BenefitProfile(profil)
                            for profil in dict.get('profils', [])]
            self.conditions = dict.get('conditions', [''])
            self.interestFlag = dict.get('interestFlag', '')
            self.type = dict.get('type', '')
            self.unit = dict.get('unit', '')
            self.periodicite = dict.get('periodicite', '')
            self.montant = dict.get('montant', None)
            self.link = dict.get('link', '')
            self.instructions = dict.get('instructions', '')
            self.teleservice = dict.get('teleservice', '')
            self.periodicite = dict.get('periodicite', '')
            self.legend = dict.get('legend', '')
        except KeyError:
            raise KeyError

    def get_profils_types(self) -> list:
        return [profil.type for profil in self.profils]
