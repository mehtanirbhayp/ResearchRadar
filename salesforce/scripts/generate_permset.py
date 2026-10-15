import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBJECTS_DIR = os.path.join(BASE_DIR, "force-app", "main", "default", "objects")
PERMSET_DIR = os.path.join(BASE_DIR, "force-app", "main", "default", "permissionsets")

objects = [
    "Research_Paper__c",
    "Research_Map__c",
    "Map_Paper_Link__c",
    "Research_Finding__c",
    "Extracted_Metric__c",
    "Research_Conflict__c",
    "Research_Gap__c"
]

tabs = [
    "Research_Map__c",
    "Research_Paper__c",
    "Research_Finding__c",
    "Research_Gap__c",
    "Research_Conflict__c"
]

field_permissions = []
object_permissions = []

for obj in objects:
    object_permissions.append(f"""    <objectPermissions>
        <allowCreate>true</allowCreate>
        <allowDelete>true</allowDelete>
        <allowEdit>true</allowEdit>
        <allowRead>true</allowRead>
        <modifyAllRecords>true</modifyAllRecords>
        <object>{obj}</object>
        <viewAllRecords>true</viewAllRecords>
    </objectPermissions>""")
    
    fields_path = os.path.join(OBJECTS_DIR, obj, "fields", "*.field-meta.xml")
    for f in glob.glob(fields_path):
        f_name = os.path.basename(f).replace(".field-meta.xml", "")
        with open(f, "r") as fp:
            content = fp.read()
            if "<type>MasterDetail</type>" in content or "<required>true</required>" in content:
                continue
            if "<type>Summary</type>" in content:
                field_permissions.append(f"""    <fieldPermissions>
        <editable>false</editable>
        <field>{obj}.{f_name}</field>
        <readable>true</readable>
    </fieldPermissions>""")
                continue
        
        field_permissions.append(f"""    <fieldPermissions>
        <editable>true</editable>
        <field>{obj}.{f_name}</field>
        <readable>true</readable>
    </fieldPermissions>""")

tab_settings = []
for t in tabs:
    tab_settings.append(f"""    <tabSettings>
        <tab>{t}</tab>
        <visibility>Visible</visibility>
    </tabSettings>""")

class_accesses = [
    f"""    <classAccesses>
        <apexClass>EreunaController</apexClass>
        <enabled>true</enabled>
    </classAccesses>""",
    f"""    <classAccesses>
        <apexClass>EreunaDataService</apexClass>
        <enabled>true</enabled>
    </classAccesses>"""
]

perm_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<PermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">
    <description>Grants full researcher and administrator access to Research Radar objects, fields, and tabs.</description>
    <hasActivationRequired>false</hasActivationRequired>
    <label>Ereuna Researcher Access</label>
{chr(10).join(class_accesses)}
{chr(10).join(sorted(field_permissions))}
{chr(10).join(object_permissions)}
{chr(10).join(tab_settings)}
</PermissionSet>
"""

os.makedirs(PERMSET_DIR, exist_ok=True)
with open(os.path.join(PERMSET_DIR, "Ereuna_Researcher_Access.permissionset-meta.xml"), "w", encoding="utf-8") as f:
    f.write(perm_xml)

print("Permission set generated successfully!")
