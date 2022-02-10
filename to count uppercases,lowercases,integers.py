import re
string = "IAMPravalikaIamfromKumarambheempin.504296"
upper_cases=re.findall(r"[A-Z]",string)
lower_cases=re.findall(r"[a-z]",string)
integers=re.findall(r"[0-9]",string)
print(len(upper_cases))
print(len(lower_cases))
print(len(integers))