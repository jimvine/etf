from marshmallow import Schema, fields, validate


class DateAndBlankField(fields.Date):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


class UserSchema(Schema):
    email = fields.Str()


class EvaluationSchema(Schema):
    # TODO - add more validation esp. for choice fields, around dates
    user = fields.Nested(UserSchema())
    id = fields.UUID()
    title = fields.Str(validate=validate.Length(max=256))
    description = fields.Str()
    topics = fields.Raw()  # TODO - this should be a JSON field
    organisation = fields.Str(validate=validate.Length(max=256))
    is_published = fields.Boolean()

    # Issue description
    issue_description = fields.Str()
    those_experiencing_issue = fields.Str()
    why_improvements_matter = fields.Str()
    who_improvements_matter_to = fields.Str()
    current_practice = fields.Str()
    issue_relevance = fields.Str()

    # Evaluation - event dates
    evaluation_start_date = DateAndBlankField(allow_none=True)
    evaluation_end_date = DateAndBlankField(allow_none=True)
    date_of_intended_publication = DateAndBlankField(allow_none=True)
    reasons_for_delays_in_publication = fields.Str()

    # Participant recruitment approach
    target_population = fields.Str()
    eligibility_criteria = fields.Str()
    process_for_recruitment = fields.Str()
    target_sample_size = fields.Str()
    intended_recruitment_schedule = fields.Str()
    date_of_first_recruitment = DateAndBlankField(allow_none=True)

    # Ethical considerations
    ethics_committee_approval = fields.Boolean()
    ethics_committee_details = fields.Str()
    ethical_state_given_existing_evidence_base = fields.Str()
    risks_to_participants = fields.Str()
    risks_to_study_team = fields.Str()
    participant_involvement = fields.Str()
    participant_consent = fields.Str()
    participant_information = fields.Str()
    participant_payment = fields.Str()
    confidentiality_and_personal_data = fields.Str()
    breaking_confidentiality = fields.Str()
    other_ethical_information = fields.Str()

    # Autogenerated fields
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class Intervention(Schema):
    evaluation = fields.Nested(EvaluationSchema())
    name = fields.Str(validate=validate.Length(max=256))
    brief_description = fields.Str()
    rationale = fields.Str()
    materials_used = fields.Str()
    procedures = fields.Str()
    provider_description = fields.Str()
    modes_of_delivery = fields.Str()
    location = fields.Str()
    frequency_of_delivery = fields.Str()
    tailoring = fields.Str()
    fidelity = fields.Str()
    resource_requirements = fields.Str()


class OutcomeMeasureSchema(Schema):
    evaluation = fields.Nested(EvaluationSchema)
    name = fields.Str(validate=validate.Length(max=256))
    primary_or_secondary = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    direct_or_surrogate = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    description = fields.Str()
    collection_process = fields.Str()
    timepoint = fields.Str()
    minimum_difference = fields.Str()
    relevance = fields.Str()
