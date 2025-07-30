from typing import Optional
def get_mongodb_execute_prompt(mongodb_output, 
                               mongodb_query, 
                               query, 
                               context,
                               tool_call_count,
                               data_retrieval_size: Optional[int]):
    
    procedures_example = ('''
    "procedures": {
        "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/procedures.py",
        "schema_version": "0.11.2",
        "subject_id": "662616",
        "subject_procedures": [
        {
            "procedure_type": "Surgery",
            "start_date": "2023-02-03",
            "experimenter_full_name": "30509",
            "iacuc_protocol": null,
            "animal_weight_prior": null,
            "animal_weight_post": null,
            "weight_unit": "gram",
            "anaesthesia": null,
            "workstation_id": null,
            "procedures": [
            {
                "procedure_type": "Perfusion",
                "protocol_id": "dx.doi.org/10.17504/protocols.io.bg5vjy66",
                "output_specimen_ids": [
                "662616"
                ]
            }
            ],
            "notes": null
        },
        {
            "procedure_type": "Surgery",
            "start_date": "2023-01-05",
            "experimenter_full_name": "NSB-5756",
            "iacuc_protocol": "2109",
            "animal_weight_prior": "16.6",
            "animal_weight_post": "16.7",
            "weight_unit": "gram",
            "anaesthesia": {
            "type": "isoflurane",
            "duration": "120.0",
            "duration_unit": "minute",
            "level": "1.5"
            },
            "workstation_id": "SWS 1",
            "procedures": [
            {
                "injection_materials": [
                {
                    "material_type": "Virus",
                    "name": "SL1-hSyn-Cre",
                    "tars_identifiers": {
                    "virus_tars_id": null,
                    "plasmid_tars_alias": null,
                    "prep_lot_number": "221118-11",
                    "prep_date": null,
                    "prep_type": null,
                    "prep_protocol": null
                    },
                    "addgene_id": null,
                    "titer": {
                    "$numberLong": "37500000000000"
                    },
                    "titer_unit": "gc/mL"
                },
                {
                    "material_type": "Virus",
                    "name": "AAV1-CAG-H2B-mTurquoise2-WPRE",
                    "tars_identifiers": {
                    "virus_tars_id": null,
                    "plasmid_tars_alias": null,
                    "prep_lot_number": "221118-4",
                    "prep_date": null,
                    "prep_type": null,
                    "prep_protocol": null
                    },
                    "addgene_id": null,
                    "titer": {
                    "$numberLong": "15000000000000"
                    },
                    "titer_unit": "gc/mL"
                }
                ],
                "recovery_time": "10.0",
                "recovery_time_unit": "minute",
                "injection_duration": null,
                "injection_duration_unit": "minute",
                "instrument_id": "NJ#2",
                "protocol_id": "dx.doi.org/10.17504/protocols.io.bgpujvnw",
                "injection_coordinate_ml": "0.35",
                "injection_coordinate_ap": "2.2",
                "injection_coordinate_depth": [
                "2.1"
                ],
                "injection_coordinate_unit": "millimeter",
                "injection_coordinate_reference": "Bregma",
                "bregma_to_lambda_distance": "4.362",
                "bregma_to_lambda_unit": "millimeter",
                "injection_angle": "0",
                "injection_angle_unit": "degrees",
                "targeted_structure": "mPFC",
                "injection_hemisphere": "Right",
                "procedure_type": "Nanoject injection",
                "injection_volume": [
                "200"
                ],
                "injection_volume_unit": "nanoliter"
            },
            {
                "injection_materials": [
                {
                    "material_type": "Virus",
                    "name": "AAV-Syn-DIO-TVA66T-dTomato-CVS N2cG",
                    "tars_identifiers": {
                    "virus_tars_id": null,
                    "plasmid_tars_alias": null,
                    "prep_lot_number": "220916-4",
                    "prep_date": null,
                    "prep_type": null,
                    "prep_protocol": null
                    },
                    "addgene_id": null,
                    "titer": {
                    "$numberLong": "18000000000000"
                    },
                    "titer_unit": "gc/mL"
                }
                ],
                "recovery_time": "10.0",
                "recovery_time_unit": "minute",
                "injection_duration": null,
                "injection_duration_unit": "minute",
                "instrument_id": "NJ#2",
                "protocol_id": "dx.doi.org/10.17504/protocols.io.bgpujvnw",
                "injection_coordinate_ml": "2.9",
                "injection_coordinate_ap": "-0.6",
                "injection_coordinate_depth": [
                "3.6"
                ],
                "injection_coordinate_unit": "millimeter",
                "injection_coordinate_reference": "Bregma",
                "bregma_to_lambda_distance": "4.362",
                "bregma_to_lambda_unit": "millimeter",
                "injection_angle": "30",
                "injection_angle_unit": "degrees",
                "targeted_structure": "VM",
                "injection_hemisphere": "Right",
                "procedure_type": "Nanoject injection",
                "injection_volume": [
                "200"
                ],
                "injection_volume_unit": "nanoliter"
            }
            ],
            "notes": null
        },
        {
            "procedure_type": "Surgery",
            "start_date": "2023-01-25",
            "experimenter_full_name": "NSB-5756",
            "iacuc_protocol": "2109",
            "animal_weight_prior": "18.6",
            "animal_weight_post": "18.7",
            "weight_unit": "gram",
            "anaesthesia": {
            "type": "isoflurane",
            "duration": "45.0",
            "duration_unit": "minute",
            "level": "1.5"
            },
            "workstation_id": "SWS 5",
            "procedures": [
            {
                "injection_materials": [
                {
                    "material_type": "Virus",
                    "name": "EnvA CVS-N2C-histone-GFP",
                    "tars_identifiers": {
                    "virus_tars_id": null,
                    "plasmid_tars_alias": null,
                    "prep_lot_number": "221110",
                    "prep_date": null,
                    "prep_type": null,
                    "prep_protocol": null
                    },
                    "addgene_id": null,
                    "titer": {
                    "$numberLong": "10700000000"
                    },
                    "titer_unit": "gc/mL"
                }
                ],
                "recovery_time": "10.0",
                "recovery_time_unit": "minute",
                "injection_duration": null,
                "injection_duration_unit": "minute",
                "instrument_id": "NJ#5",
                "protocol_id": "dx.doi.org/10.17504/protocols.io.bgpujvnw",
                "injection_coordinate_ml": "2.9",
                "injection_coordinate_ap": "-0.6",
                "injection_coordinate_depth": [
                "3.6"
                ],
                "injection_coordinate_unit": "millimeter",
                "injection_coordinate_reference": "Bregma",
                "bregma_to_lambda_distance": "4.362",
                "bregma_to_lambda_unit": "millimeter",
                "injection_angle": "30",
                "injection_angle_unit": "degrees",
                "targeted_structure": "VM",
                "injection_hemisphere": "Right",
                "procedure_type": "Nanoject injection",
                "injection_volume": [
                "200"
                ],
                "injection_volume_unit": "nanoliter"
            }
            ],
            "notes": null
        }
        ],
        "specimen_procedures": [
        {
            "procedure_type": "Fixation",
            "procedure_name": "SHIELD OFF",
            "specimen_id": "662616",
            "start_date": "2023-02-10",
            "end_date": "2023-02-12",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "SHIELD Epoxy",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            },
            {
                "name": "SHIELD Buffer",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        },
        {
            "procedure_type": "Fixation",
            "procedure_name": "SHIELD ON",
            "specimen_id": "662616",
            "start_date": "2023-02-12",
            "end_date": "2023-02-13",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "SHIELD ON",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        },
        {
            "procedure_type": "Delipidation",
            "procedure_name": "24h Delipidation",
            "specimen_id": "662616",
            "start_date": "2023-02-15",
            "end_date": "2023-02-16",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "Delipidation Buffer",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        },
        {
            "procedure_type": "Delipidation",
            "procedure_name": "Active Delipidation",
            "specimen_id": "662616",
            "start_date": "2023-02-16",
            "end_date": "2023-02-18",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "Conduction Buffer",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        },
        {
            "procedure_type": "Refractive index matching",
            "procedure_name": "50% EasyIndex",
            "specimen_id": "662616",
            "start_date": "2023-02-19",
            "end_date": "2023-02-20",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "EasyIndex",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        },
        {
            "procedure_type": "Refractive index matching",
            "procedure_name": "100% EasyIndex",
            "specimen_id": "662616",
            "start_date": "2023-02-20",
            "end_date": "2023-02-21",
            "experimenter_full_name": "DT",
            "protocol_id": "none",
            "reagents": [
            {
                "name": "EasyIndex",
                "source": "LiveCanvas Technologies",
                "rrid": null,
                "lot_number": "unknown",
                "expiration_date": null
            }
            ],
            "hcr_series": null,
            "immunolabeling": null,
            "notes": "None"
        }
        ],
        "notes": null
    },
    '''
    
    )

    things_to_note = (
        '''
        ALWAYS unwind nested procedure fields (e.g., {'\$unwind': '\$procedures.subject_procedures.procedures'})
        Use \$unwind for any array fields
        For modality queries, access data_description.modality.name
        Use \$regex instead of \$elemmatch (e.g., {"field": {"\$regex": "term", "\$options": "i"}})
        Be careful with duration queries; don't use \$subtract as durations are stored as strings
        Ignore created and last_modified fields as they're only metadata
        Example query: What is the total duration of the imaging session for the subject in SmartSPIM_662616_2023-04-14_15-11-04?
        Example MONGODB Query:  [{'$match': {'name': 'SmartSPIM_662616_2023-04-14_15-11-04'}}]
        '''
    )

    mongodb_prompt = ("Your goal is to follow the instructions below very carefully."
                      "You are orchestrating tool access to a mongodb database"
                      "If the tool executed successfully, this is the response retrieved"
                      f" by the tool [{mongodb_output}]. This was the query used, [{mongodb_query}]." 
                      f"If there is a response, ensure that it can be used to answer the user's query [{query}]. "
                      "Ignore the syntax in which the response exists, and just process the information the tools retrieved. "
                      "If the output doesn't answer the question, think about how you can change the tool call to achieve an optimal result."
                      "If it answers the query stop tool calling immediately. When summarizing the tool result, "
                      "be conscise, while ensuring all the information requested by the user is present."
                      "If it requires more context, continue. Create an appropriate mongodb query or aggregation pipeline "
                      f"based on the following texts: {context} and execute the query. For queries about procedures, use this example"
                      f" of a filled out proceudres class in an asset to get more context on how fields are nested: {procedures_example}" 
                      f"Start with a simple query and refine only if necessary. Here are some things to note: {things_to_note}"
                      f"Optimize Data Retrieval:"
                      f"Large assets can have up to 15,000 fields. If retrieval size exceeds 15,000, refine the query before executing:\n"
                      f" Use projection to select only necessary fields.\n"
                      f" Apply the `limit` filter.\n"
                      f" Use the `get_retrieval_size` tool only if necessary to estimate result size.\n"
                      f"This is the size of data retrieval: {data_retrieval_size}. "
                      "4. **Tool Call Limits:**\n"
                      f"This is the tool call count number ({tool_call_count})"
                      "   - If tool_call_count exceeds 3, do **not** use any more tools.\n"
                      "   - Proceed with summarizing what information has been gathered so far.\n\n"
                    )
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{mongodb_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages