from yankee.json.schema import fields as f
from yankee.json.schema import Schema

from .shared import DocumentStructureSchema


class PublicSearchBiblioSchema(Schema):
    guid = f.String("guid")

    appl_id = f.String("applicationNumber")
    app_filing_date = f.Date("applicationFilingDate.0")
    related_appl_filing_date = f.List(f.Date, "relatedApplFilingDate")
    publication_number = f.String("publicationReferenceDocumentNumber")
    kind_code = f.String("kindCode.0")
    publication_date = f.Date("datePublished")
    patent_title = f.String("inventionTitle")

    inventors_short = f.String("inventorsShort")
    applicant_name = f.List(f.String, "applicantName")
    assignee_name = f.List(f.String, "assigneeName")
    government_interest = f.List(f.String, "governmentInterest")
    primary_examiner = f.String("primaryExaminer")
    assistant_examiner = f.List(f.String, "assistantExaminer")

    main_classification_code = f.String("mainClassificationCode")
    cpc_additional = f.DelimitedString(f.Str(), "cpcAdditionalFlattened", delimeter=";")
    cpc_inventive = f.DelimitedString(f.Str(), "cpcInventiveFlattened", delimeter=";")
    ipc_code = f.DelimitedString(f.Str(), "ipcCodeFlattened", delimeter=";")
    uspc_full_classification = f.DelimitedString(f.Str(), "uspcFullClassificationFlattened", delimeter=";")

    image_file_name = f.String("imageFileName")
    image_location = f.String("imageLocation")
    document_structure = DocumentStructureSchema(data_key=False)

    type = f.String("type")
    database_name = f.String("databaseName")
    composite_id = f.String("compositeId")
    document_id = f.String("documentId")
    document_size = f.Integer("documentSize")
    family_identifier_cur = f.Integer("familyIdentifierCur")
    language_indicator = f.String("languageIndicator")

    score = f.Float("score")


class PublicSearchBiblioPageSchema(Schema):
    num_found = f.Integer("numFound")
    per_page = f.Integer("perPage")
    page = f.Integer("page")
    docs = f.List(PublicSearchBiblioSchema, "patents")
