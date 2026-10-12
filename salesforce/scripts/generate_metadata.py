import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(BASE_DIR, "force-app", "main", "default")
OBJECTS_DIR = os.path.join(DEFAULT_DIR, "objects")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

def make_obj_meta(label, plural_label, name_field_type="Text", name_field_label="Name", sharing_model="ReadWrite"):
    if name_field_type == "AutoNumber":
        name_xml = f"""    <nameField>
        <displayFormat>R-{{0000}}</displayFormat>
        <label>{name_field_label}</label>
        <type>AutoNumber</type>
    </nameField>"""
    else:
        name_xml = f"""    <nameField>
        <label>{name_field_label}</label>
        <type>Text</type>
    </nameField>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <actionOverrides>
        <actionName>Accept</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>CancelEdit</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>Clone</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>Delete</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>Edit</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>List</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>New</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>SaveEdit</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>Tab</actionName>
        <type>Default</type>
    </actionOverrides>
    <actionOverrides>
        <actionName>View</actionName>
        <type>Default</type>
    </actionOverrides>
    <allowInChatterGroups>false</allowInChatterGroups>
    <compactLayoutAssignment>SYSTEM</compactLayoutAssignment>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableActivities>true</enableActivities>
    <enableBulkApi>true</enableBulkApi>
    <enableFeeds>false</enableFeeds>
    <enableHistory>true</enableHistory>
    <enableLicensing>false</enableLicensing>
    <enableReports>true</enableReports>
    <enableSearch>true</enableSearch>
    <enableSharing>true</enableSharing>
    <enableStreamingApi>true</enableStreamingApi>
    <label>{label}</label>
{name_xml}
    <pluralLabel>{plural_label}</pluralLabel>
    <sharingModel>{sharing_model}</sharingModel>
    <visibility>Public</visibility>
</CustomObject>"""

def field_text(label, length=255, required=False, unique=False, external_id=False):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>{'true' if external_id else 'false'}</externalId>
    <label>{label.replace('_', ' ')}</label>
    <length>{length}</length>
    <required>{'true' if required else 'false'}</required>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Text</type>
    <unique>{'true' if unique else 'false'}</unique>
</CustomField>"""

def field_long_text(label, length=32000, lines=4):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <length>{length}</length>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>LongTextArea</type>
    <visibleLines>{lines}</visibleLines>
</CustomField>"""

def field_number(label, precision=18, scale=0, default_val=None, required=False):
    def_tag = f"\n    <defaultValue>{default_val}</defaultValue>" if default_val is not None else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>{def_tag}
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <precision>{precision}</precision>
    <required>{'true' if required else 'false'}</required>
    <scale>{scale}</scale>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Number</type>
    <unique>false</unique>
</CustomField>"""

def field_percent(label, precision=5, scale=2):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <precision>{precision}</precision>
    <required>false</required>
    <scale>{scale}</scale>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Percent</type>
</CustomField>"""

def field_url(label):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <required>false</required>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Url</type>
</CustomField>"""

def field_picklist(label, values, default_val=None):
    values_xml = []
    for v in values:
        is_def = "true" if v == default_val else "false"
        values_xml.append(f"""            <value>
                <fullName>{v}</fullName>
                <default>{is_def}</default>
                <label>{v}</label>
            </value>""")
    val_set = "\n".join(values_xml)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <required>false</required>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Picklist</type>
    <valueSet>
        <restricted>true</restricted>
        <valueSetDefinition>
            <sorted>false</sorted>
{val_set}
        </valueSetDefinition>
    </valueSet>
</CustomField>"""

def field_lookup(label, ref_to, relationship_name):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <deleteConstraint>SetNull</deleteConstraint>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <referenceTo>{ref_to}</referenceTo>
    <relationshipLabel>{label.replace('_', ' ')}</relationshipLabel>
    <relationshipName>{relationship_name}</relationshipName>
    <required>false</required>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Lookup</type>
</CustomField>"""

def field_master_detail(label, ref_to, relationship_name, rel_label):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <referenceTo>{ref_to}</referenceTo>
    <relationshipLabel>{rel_label}</relationshipLabel>
    <relationshipName>{relationship_name}</relationshipName>
    <relationshipOrder>0</relationshipOrder>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>MasterDetail</type>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
</CustomField>"""

def field_summary_count(label, foreign_key):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{label}__c</fullName>
    <externalId>false</externalId>
    <label>{label.replace('_', ' ')}</label>
    <summaryForeignKey>{foreign_key}</summaryForeignKey>
    <summaryOperation>count</summaryOperation>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>Summary</type>
</CustomField>"""

def validation_rule(name, error_cond, error_msg, display_field=None):
    field_tag = f"\n    <errorDisplayField>{display_field}</errorDisplayField>" if display_field else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ValidationRule xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>{name}</fullName>
    <active>true</active>
    <errorConditionFormula>{error_cond}</errorConditionFormula>{field_tag}
    <errorMessage>{error_msg}</errorMessage>
</ValidationRule>"""

def generate():
    # 1. Research_Paper__c
    p_dir = os.path.join(OBJECTS_DIR, "Research_Paper__c")
    write_file(os.path.join(p_dir, "Research_Paper__c.object-meta.xml"),
               make_obj_meta("Research Paper", "Research Papers", name_field_label="Paper Name"))
    
    p_fields = os.path.join(p_dir, "fields")
    write_file(os.path.join(p_fields, "Title__c.field-meta.xml"), field_text("Title", 255, required=True))
    write_file(os.path.join(p_fields, "Authors__c.field-meta.xml"), field_long_text("Authors", 32000, 3))
    write_file(os.path.join(p_fields, "DOI__c.field-meta.xml"), field_text("DOI", 100, external_id=True, unique=True))
    write_file(os.path.join(p_fields, "Publication_Year__c.field-meta.xml"), field_number("Publication_Year", 4, 0))
    write_file(os.path.join(p_fields, "Venue__c.field-meta.xml"), field_text("Venue", 255))
    write_file(os.path.join(p_fields, "Abstract__c.field-meta.xml"), field_long_text("Abstract", 32000, 5))
    write_file(os.path.join(p_fields, "Citation_Count__c.field-meta.xml"), field_number("Citation_Count", 8, 0, default_val=0))
    write_file(os.path.join(p_fields, "Open_Access_URL__c.field-meta.xml"), field_url("Open_Access_URL"))
    write_file(os.path.join(p_fields, "PDF_URL__c.field-meta.xml"), field_url("PDF_URL"))
    write_file(os.path.join(p_fields, "BibTeX__c.field-meta.xml"), field_long_text("BibTeX", 32000, 5))
    write_file(os.path.join(p_fields, "Primary_Discipline__c.field-meta.xml"),
               field_picklist("Primary_Discipline", ["Computer Science", "Artificial Intelligence", "Biomedicine", "Cloud Computing", "Distributed Systems"], "Cloud Computing"))
    
    p_val = os.path.join(p_dir, "validationRules")
    write_file(os.path.join(p_val, "VR_Publication_Year_Range.validationRule-meta.xml"),
               validation_rule("VR_Publication_Year_Range",
                               "Publication_Year__c > YEAR(TODAY()) || Publication_Year__c < 1900",
                               "Publication Year must be between 1900 and the current year.",
                               "Publication_Year__c"))
    write_file(os.path.join(p_val, "VR_Valid_DOI_Prefix.validationRule-meta.xml"),
               validation_rule("VR_Valid_DOI_Prefix",
                               "NOT(ISBLANK(DOI__c)) && NOT(BEGINS(DOI__c, '10.'))",
                               "DOI must begin with the standard prefix '10.' (e.g., 10.1145/...)",
                               "DOI__c"))

    # 2. Research_Map__c
    m_dir = os.path.join(OBJECTS_DIR, "Research_Map__c")
    write_file(os.path.join(m_dir, "Research_Map__c.object-meta.xml"),
               make_obj_meta("Research Map", "Research Maps", name_field_type="AutoNumber", name_field_label="Map Number"))
    
    m_fields = os.path.join(m_dir, "fields")
    write_file(os.path.join(m_fields, "Topic__c.field-meta.xml"), field_text("Topic", 255, required=True))
    write_file(os.path.join(m_fields, "Status__c.field-meta.xml"),
               field_picklist("Status", ["Draft", "In Progress", "Synthesized", "Archived"], "Draft"))
    write_file(os.path.join(m_fields, "Synthesis_Summary__c.field-meta.xml"), field_long_text("Synthesis_Summary", 32000, 5))
    write_file(os.path.join(m_fields, "Target_Discipline__c.field-meta.xml"),
               field_picklist("Target_Discipline", ["Computer Science", "Artificial Intelligence", "Biomedicine", "Cloud Computing", "Distributed Systems"], "Cloud Computing"))
    write_file(os.path.join(m_fields, "Total_Papers__c.field-meta.xml"), field_summary_count("Total_Papers", "Map_Paper_Link__c.Research_Map__c"))
    write_file(os.path.join(m_fields, "Total_Findings__c.field-meta.xml"), field_summary_count("Total_Findings", "Research_Finding__c.Research_Map__c"))
    write_file(os.path.join(m_fields, "Total_Gaps__c.field-meta.xml"), field_summary_count("Total_Gaps", "Research_Gap__c.Research_Map__c"))
    write_file(os.path.join(m_fields, "Total_Conflicts__c.field-meta.xml"), field_summary_count("Total_Conflicts", "Research_Conflict__c.Research_Map__c"))

    m_val = os.path.join(m_dir, "validationRules")
    write_file(os.path.join(m_val, "VR_Synthesized_Map_Needs_Summary.validationRule-meta.xml"),
               validation_rule("VR_Synthesized_Map_Needs_Summary",
                               "ISPICKVAL(Status__c, 'Synthesized') && ISBLANK(Synthesis_Summary__c)",
                               "A Research Map cannot be marked Synthesized without an AI/Literature synthesis summary.",
                               "Synthesis_Summary__c"))

    # 3. Map_Paper_Link__c (Junction)
    j_dir = os.path.join(OBJECTS_DIR, "Map_Paper_Link__c")
    write_file(os.path.join(j_dir, "Map_Paper_Link__c.object-meta.xml"),
               make_obj_meta("Map Paper Link", "Map Paper Links", name_field_type="AutoNumber", name_field_label="Link ID", sharing_model="ControlledByParent"))
    
    j_fields = os.path.join(j_dir, "fields")
    write_file(os.path.join(j_fields, "Research_Map__c.field-meta.xml"),
               field_master_detail("Research_Map", "Research_Map__c", "Map_Paper_Links", "Map Paper Links"))
    # Second master-detail
    j_paper_md = f"""<?xml version="1.0" encoding="UTF-8"?>
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Research_Paper__c</fullName>
    <externalId>false</externalId>
    <label>Research Paper</label>
    <referenceTo>Research_Paper__c</referenceTo>
    <relationshipLabel>Associated Maps</relationshipLabel>
    <relationshipName>Map_Paper_Links</relationshipName>
    <relationshipOrder>1</relationshipOrder>
    <reparentableMasterDetail>false</reparentableMasterDetail>
    <trackHistory>false</trackHistory>
    <trackTrending>false</trackTrending>
    <type>MasterDetail</type>
    <writeRequiresMasterRead>false</writeRequiresMasterRead>
</CustomField>"""
    write_file(os.path.join(j_fields, "Research_Paper__c.field-meta.xml"), j_paper_md)
    write_file(os.path.join(j_fields, "Relevance_Score__c.field-meta.xml"), field_percent("Relevance_Score", 5, 2))
    write_file(os.path.join(j_fields, "Inclusion_Rationale__c.field-meta.xml"), field_text("Inclusion_Rationale", 255))

    # 4. Research_Finding__c
    f_dir = os.path.join(OBJECTS_DIR, "Research_Finding__c")
    write_file(os.path.join(f_dir, "Research_Finding__c.object-meta.xml"),
               make_obj_meta("Research Finding", "Research Findings", name_field_type="AutoNumber", name_field_label="Finding ID", sharing_model="ControlledByParent"))
    
    f_fields = os.path.join(f_dir, "fields")
    write_file(os.path.join(f_fields, "Research_Map__c.field-meta.xml"),
               field_master_detail("Research_Map", "Research_Map__c", "Research_Findings", "Research Findings"))
    write_file(os.path.join(f_fields, "Research_Paper__c.field-meta.xml"),
               field_lookup("Research_Paper", "Research_Paper__c", "Research_Findings"))
    write_file(os.path.join(f_fields, "Claim_Summary__c.field-meta.xml"), field_text("Claim_Summary", 255, required=True))
    write_file(os.path.join(f_fields, "Exact_Quote__c.field-meta.xml"), field_long_text("Exact_Quote", 5000, 3))
    write_file(os.path.join(f_fields, "Page_Number__c.field-meta.xml"), field_number("Page_Number", 4, 0))
    write_file(os.path.join(f_fields, "Section_Name__c.field-meta.xml"), field_text("Section_Name", 100))
    write_file(os.path.join(f_fields, "Verification_Status__c.field-meta.xml"),
               field_picklist("Verification_Status", ["Extracted", "Verified", "Disputed", "Unverified"], "Extracted"))
    write_file(os.path.join(f_fields, "Confidence_Score__c.field-meta.xml"), field_percent("Confidence_Score", 5, 2))

    f_val = os.path.join(f_dir, "validationRules")
    write_file(os.path.join(f_val, "VR_Verified_Finding_Needs_Quote.validationRule-meta.xml"),
               validation_rule("VR_Verified_Finding_Needs_Quote",
                               "ISPICKVAL(Verification_Status__c, 'Verified') && (ISBLANK(Exact_Quote__c) || ISBLANK(Page_Number__c))",
                               "A verified claim must include the exact verbatim quote and the page number where it appears.",
                               "Exact_Quote__c"))

    # 5. Extracted_Metric__c
    met_dir = os.path.join(OBJECTS_DIR, "Extracted_Metric__c")
    write_file(os.path.join(met_dir, "Extracted_Metric__c.object-meta.xml"),
               make_obj_meta("Extracted Metric", "Extracted Metrics", name_field_type="AutoNumber", name_field_label="Metric ID", sharing_model="ControlledByParent"))
    
    met_fields = os.path.join(met_dir, "fields")
    write_file(os.path.join(met_fields, "Research_Paper__c.field-meta.xml"),
               field_master_detail("Research_Paper", "Research_Paper__c", "Extracted_Metrics", "Extracted Metrics"))
    write_file(os.path.join(met_fields, "Metric_Name__c.field-meta.xml"), field_text("Metric_Name", 100, required=True))
    write_file(os.path.join(met_fields, "Metric_Value__c.field-meta.xml"), field_number("Metric_Value", 12, 4))
    write_file(os.path.join(met_fields, "Unit__c.field-meta.xml"), field_text("Unit", 30))
    write_file(os.path.join(met_fields, "Benchmark_Dataset__c.field-meta.xml"), field_text("Benchmark_Dataset", 100))
    write_file(os.path.join(met_fields, "Notes__c.field-meta.xml"), field_text("Notes", 255))

    # 6. Research_Conflict__c
    c_dir = os.path.join(OBJECTS_DIR, "Research_Conflict__c")
    write_file(os.path.join(c_dir, "Research_Conflict__c.object-meta.xml"),
               make_obj_meta("Research Conflict", "Research Conflicts", name_field_type="AutoNumber", name_field_label="Conflict ID", sharing_model="ControlledByParent"))
    
    c_fields = os.path.join(c_dir, "fields")
    write_file(os.path.join(c_fields, "Research_Map__c.field-meta.xml"),
               field_master_detail("Research_Map", "Research_Map__c", "Research_Conflicts", "Research Conflicts"))
    write_file(os.path.join(c_fields, "Paper_A__c.field-meta.xml"), field_lookup("Paper_A", "Research_Paper__c", "Conflicts_As_Paper_A"))
    write_file(os.path.join(c_fields, "Paper_B__c.field-meta.xml"), field_lookup("Paper_B", "Research_Paper__c", "Conflicts_As_Paper_B"))
    write_file(os.path.join(c_fields, "Disagreement_Area__c.field-meta.xml"), field_text("Disagreement_Area", 255, required=True))
    write_file(os.path.join(c_fields, "Conflict_Description__c.field-meta.xml"), field_long_text("Conflict_Description", 5000, 3))
    write_file(os.path.join(c_fields, "Severity__c.field-meta.xml"),
               field_picklist("Severity", ["Low", "Moderate", "Direct Contradiction"], "Moderate"))

    # 7. Research_Gap__c
    g_dir = os.path.join(OBJECTS_DIR, "Research_Gap__c")
    write_file(os.path.join(g_dir, "Research_Gap__c.object-meta.xml"),
               make_obj_meta("Research Gap", "Research Gaps", name_field_type="AutoNumber", name_field_label="Gap ID", sharing_model="ControlledByParent"))
    
    g_fields = os.path.join(g_dir, "fields")
    write_file(os.path.join(g_fields, "Research_Map__c.field-meta.xml"),
               field_master_detail("Research_Map", "Research_Map__c", "Research_Gaps", "Research Gaps"))
    write_file(os.path.join(g_fields, "Problem_Statement__c.field-meta.xml"), field_text("Problem_Statement", 255, required=True))
    write_file(os.path.join(g_fields, "Proposed_Experiment__c.field-meta.xml"), field_long_text("Proposed_Experiment", 5000, 4))
    write_file(os.path.join(g_fields, "Priority__c.field-meta.xml"),
               field_picklist("Priority", ["Low", "Medium", "High"], "Medium"))
    write_file(os.path.join(g_fields, "Estimated_Complexity__c.field-meta.xml"),
               field_picklist("Estimated_Complexity", ["Low", "Medium", "High"], "Medium"))
    write_file(os.path.join(g_fields, "Status__c.field-meta.xml"),
               field_picklist("Status", ["Identified", "In Review", "Experiment Drafted", "Addressed"], "Identified"))

    print("All custom objects and fields generated successfully!")

if __name__ == "__main__":
    generate()
