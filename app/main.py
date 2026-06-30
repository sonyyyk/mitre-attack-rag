from app.mitre.parser import MITREParser

parser = MITREParser()

attack_patterns = parser.get_attack_patterns()

print(attack_patterns[0])