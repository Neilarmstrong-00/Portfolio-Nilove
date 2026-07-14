import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=7': 'img/NILOVE_MANDAL_Portfoio.pdf#page=11',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=3': 'img/NILOVE_MANDAL_Portfoio.pdf#page=4',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=5': 'img/NILOVE_MANDAL_Portfoio.pdf#page=6',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=10': 'img/NILOVE_MANDAL_Portfoio.pdf#page=13',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=14': 'img/NILOVE_MANDAL_Portfoio.pdf#page=17',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=9': 'img/NILOVE_MANDAL_Portfoio.pdf#page=12',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=12': 'img/NILOVE_MANDAL_Portfoio.pdf#page=15',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=17': 'img/NILOVE_MANDAL_Portfoio.pdf#page=20',
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=20': 'img/NILOVE_MANDAL_Portfoio.pdf#page=23',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Special handling for the two #page=18 instances
# First one is Biometric Attendance (Line 448)
content = content.replace(
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=18\', \'View Documentation\')\">\n                    <div class="font-mono text-neon-cyan text-xs mb-3">008',
    'img/NILOVE_MANDAL_Portfoio.pdf#page=21\', \'View Documentation\')">\n                    <div class="font-mono text-neon-cyan text-xs mb-3">008'
)

# Second one is Precision Seeding Unit (Line 464)
content = content.replace(
    'img/Project_and_Design_Portfolio_Nilove_Mandal.pdf#page=18\', \'View Documentation\')">\n                    <div class="font-mono text-neon-cyan text-xs mb-3">009',
    'img/NILOVE_MANDAL_Portfoio.pdf#page=19\', \'View Documentation\')">\n                    <div class="font-mono text-neon-cyan text-xs mb-3">009'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates successful.")
