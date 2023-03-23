import frappe
import json


@frappe.whitelist()
def get_doctype_meta(doctype):
    meta = frappe.get_meta(doctype)
    return meta


@frappe.whitelist()
def select_property_list(doctype):
    allowed_fields = []
    exclude_fields = ["naming_series", "employee", "first_name", "middle_name", "last_name", "marital_status", "ctc",
                      "employee_name", "status", "image", "gender", "date_of_birth", "date_of_joining", "lft", "rgt",
                      "old_parent"]
    exclude_field_types = ["HTML", "Section Break", "Column Break", "Button", "Read Only", "Tab Break", "Table"]

    meta = get_doctype_meta(doctype)

    field_label_map = {}
    for field in meta.fields:
        field_label_map[field.fieldname] = "{} ({})".format(field.label, field.fieldname)
        if field.fieldtype not in exclude_field_types \
                and field.fieldname not in exclude_fields \
                and not field.hidden \
                and not field.read_only:
            allowed_fields.append({
                "label": field_label_map[field.fieldname],
                "feildname": field.fieldname
            })

    return allowed_fields

