from marshmallow import Schema, fields, validate

from . import choices


class DateAndBlankField(fields.Date):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


class FloatAndBlankField(fields.Float):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


class IntAndBlankField(fields.Int):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


def is_non_neg_int_or_none(value):
    error = validate.ValidationError("Value should be a non-negative integer")
    if not isinstance(value, int):
        if not value:
            value = None
        else:
            raise error
    elif value < 0:
        raise error


class UserSchema(Schema):
    email = fields.Str()


class TimeStampedModelSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class EvaluationSchema(TimeStampedModelSchema):
    # TODO - add more validation esp. for choice fields, around dates
    users = fields.Function(lambda e: UserSchema(many=True).dump(e.users.all()))
    id = fields.UUID()
    title = fields.Str(required=True, validate=validate.Length(max=256))
    short_title = fields.Str(validate=validate.Length(max=64))
    brief_description = fields.Str()
    topics = fields.Raw()
    organisations = fields.Raw()
    status = fields.Str(
        validate=validate.And(
            validate.OneOf(choices.get_db_values(choices.EvaluationStatus.choices)), validate.Length(max=256)
        ),
        default=choices.EvaluationStatus.DRAFT.value,
    )

    doi = fields.Str(validate=validate.Length(max=64))
    page_statuses = fields.Raw()

    # Issue description
    issue_description = fields.Str()
    those_experiencing_issue = fields.Str()
    why_improvements_matter = fields.Str()
    who_improvements_matter_to = fields.Str()
    current_practice = fields.Str()
    issue_relevance = fields.Str()

    # Evaluation costs and budget
    costs = fields.Function(lambda e: EvaluationCostSchema(many=True, exclude=("evaluation",)).dump(e.costs.all()))

    # Documents
    documents = fields.Function(lambda e: DocumentSchema(many=True, exclude=("evaluation",)).dump(e.documents.all()))

    # Event dates
    event_dates = fields.Function(
        lambda e: EventDateSchema(many=True, exclude=("evaluation",)).dump(e.event_dates.all())
    )

    # Evaluation type
    evaluation_type = fields.Raw()
    evaluation_type_other = fields.Str(validate=validate.Length(max=256))

    # Studied population
    studied_population = fields.Str()
    eligibility_criteria = fields.Str()
    sample_size = IntAndBlankField(validate=is_non_neg_int_or_none, allow_none=True)
    sample_size_units = fields.Str(validate=validate.Length(max=256))
    sample_size_details = fields.Str()

    # Participant recruitment approach
    process_for_recruitment = fields.Str()
    recruitment_schedule = fields.Str()

    # Ethical considerations
    ethics_committee_approval = fields.Str(
        validate=validate.And(validate.OneOf(choices.get_db_values(choices.YesNo.choices)), validate.Length(max=3))
    )
    ethics_committee_details = fields.Str()
    ethical_state_given_existing_evidence_base = fields.Str()
    risks_to_participants = fields.Str()
    risks_to_study_team = fields.Str()
    participant_involvement = fields.Str()
    participant_information = fields.Str()
    participant_consent = fields.Str()
    participant_payment = fields.Str()
    confidentiality_and_personal_data = fields.Str()
    breaking_confidentiality = fields.Str()
    other_ethical_information = fields.Str()

    # Impact evaluation design
    impact_eval_design_name = fields.Raw()
    impact_eval_design_name_other = fields.Str(validate=validate.Length(max=64))
    impact_eval_design_justification = fields.Str()
    impact_eval_design_description = fields.Str()
    impact_eval_design_features = fields.Str()
    impact_eval_design_equity = fields.Str()
    impact_eval_design_assumptions = fields.Str()
    impact_eval_design_approach_limitations = fields.Str()

    # Impact evaluation analysis
    impact_eval_framework = fields.Str(
        validate=validate.And(
            validate.OneOf(choices.get_db_values(choices.ImpactFramework.choices)), validate.Length(max=64)
        )
    )
    impact_eval_framework_other = fields.Str(validate=validate.Length(max=256))
    impact_eval_basis = fields.Str(
        validate=validate.And(
            validate.OneOf(choices.get_db_values(choices.ImpactAnalysisBasis.choices)), validate.Length(max=64)
        )
    )
    impact_eval_basis_other = fields.Str(validate=validate.Length(max=256))
    impact_eval_analysis_set = fields.Str()
    impact_eval_effect_measure_type = fields.Str(validate=validate.Length(max=64))
    impact_eval_primary_effect_size_measure = fields.Str()
    impact_eval_effect_measure_interval = fields.Str(
        validate=validate.And(
            validate.OneOf(choices.get_db_values(choices.ImpactMeasureInterval.choices)), validate.Length(max=64)
        )
    )
    impact_eval_effect_measure_interval_other = fields.Str(validate=validate.Length(max=256))
    impact_eval_primary_effect_size_desc = fields.Str()
    impact_eval_interpretation_type = fields.Str(
        validate=validate.And(
            validate.OneOf(choices.get_db_values(choices.ImpactEvalInterpretation.choices)), validate.Length(max=64)
        )
    )
    impact_eval_interpretation_type_other = fields.Str(validate=validate.Length(max=256))
    impact_eval_sensitivity_analysis = fields.Str()
    impact_eval_subgroup_analysis = fields.Str()
    impact_eval_missing_data_handling = fields.Str()
    impact_eval_fidelity = fields.Str(
        validate=validate.And(validate.Length(max=10), validate.OneOf(choices.get_db_values(choices.YesNo.choices)))
    )
    impact_eval_desc_planned_analysis = fields.Str()

    # Process evaluation design
    process_eval_methods = fields.Str(validate=validate.Length(max=256))

    # Process evaluation analysis
    process_eval_analysis_description = fields.Str()

    # Economic evaluation design
    economic_eval_type = fields.Str(
        validate=validate.And(
            validate.Length(max=256), validate.OneOf(choices.get_db_values(choices.EconomicEvaluationType.choices))
        )
    )
    perspective_costs = fields.Str()
    perspective_benefits = fields.Str()
    monetisation_approaches = fields.Str()
    economic_eval_design_details = fields.Str()

    # Economic evaluation analysis
    economic_eval_analysis_description = fields.Str()

    # Other evaluation design
    other_eval_design_type = fields.Str()
    other_eval_design_details = fields.Str()

    # Other evaluation analysis
    other_eval_analysis_description = fields.Str()

    # Interventions
    interventions = fields.Function(
        lambda e: InterventionSchema(many=True, exclude=("evaluation",)).dump(e.interventions.all())
    )

    # Outcome measures
    outcome_measures = fields.Function(
        lambda e: OutcomeMeasureSchema(many=True, exclude=("evaluation",)).dump(e.outcome_measures.all())
    )

    # Other measurement
    other_measures = fields.Function(
        lambda e: OtherMeasureSchema(many=True, exclude=("evaluation",)).dump(e.other_measures.all())
    )

    # Impact evaluation findings
    impact_eval_comparison = fields.Str()
    impact_eval_outcome = fields.Str()
    impact_eval_interpretation = fields.Str(validate=validate.Length(max=256))
    impact_eval_point_estimate_diff = fields.Str()
    impact_eval_lower_uncertainty = fields.Str()
    impact_eval_upper_uncertainty = fields.Str()

    # Economic evaluation findings
    economic_eval_summary_findings = fields.Str()
    economic_eval_findings = fields.Str()

    # Process evaluation findings
    process_eval_summary_findings = fields.Str()
    process_eval_findings = fields.Str()

    # Other evaluation findings
    other_eval_summary_findings = fields.Str()
    other_eval_findings = fields.Str()

    # Processes and standards
    process_standards = fields.Function(
        lambda e: ProcessStandardSchema(many=True, exclude=("evaluation",)).dump(e.process_standards.all())
    )

    # Links and IDs
    link_other_services = fields.Function(
        lambda e: LinkOtherServiceSchema(many=True, exclude=("evaluation",)).dump(e.link_other_services.all())
    )

    search_text = fields.Str()


class InterventionSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema())
    id = fields.UUID(dump_only=True)
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
    geographical_information = fields.Str()


class OutcomeMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    primary_or_secondary = fields.Str(
        validate=validate.And(
            validate.Length(max=10), validate.OneOf(choices.get_db_values(choices.OutcomeType.choices))
        )
    )
    direct_or_surrogate = fields.Str(
        validate=validate.And(
            validate.Length(max=10), validate.OneOf(choices.get_db_values(choices.OutcomeMeasure.choices))
        )
    )
    measure_type = fields.Str(
        validate=validate.And(
            validate.Length(max=256), validate.OneOf(choices.get_db_values(choices.MeasureType.choices))
        )
    )
    measure_type_other = fields.Str(validate=validate.Length(max=256))
    description = fields.Str()
    collection_process = fields.Str()
    timepoint = fields.Str()
    minimum_difference = fields.Str()
    relevance = fields.Str()


class OtherMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    measure_type = fields.Str(
        validate=validate.And(
            validate.Length(max=256), validate.OneOf(choices.get_db_values(choices.MeasureType.choices))
        )
    )
    measure_type_other = fields.Str(validate=validate.Length(max=256))
    description = fields.Str()
    collection_process = fields.Str()


class ProcessStandardSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    conformity = fields.Str(
        validate=validate.And(
            validate.Length(max=10), validate.OneOf(choices.get_db_values(choices.FullNoPartial.choices))
        )
    )
    description = fields.Str()


class DocumentSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    title = fields.Str(validate=validate.Length(max=256))
    url = fields.Url(validate=validate.Length(max=512))
    description = fields.Str()
    document_types = fields.Raw()
    document_type_other = fields.Str(validate=validate.Length(max=256))


class EventDateSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    event_date_name = fields.Str(validate=validate.Length(max=256))
    date = DateAndBlankField()
    event_date_type = fields.Str(
        validate=validate.And(
            validate.Length(max=10), validate.OneOf(choices.get_db_values(choices.EventDateType.choices))
        )
    )
    reasons_for_change = fields.Str()


class LinkOtherServiceSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    name_of_service = fields.Str(validate=validate.Length(max=256))
    link_or_identifier = fields.Str(validate=validate.Length(max=256))


class EvaluationCostSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    item_name = fields.Str()
    description = fields.Str()
    item_cost = FloatAndBlankField()
    earliest_spend_date = DateAndBlankField()
    latest_spend_date = DateAndBlankField()
