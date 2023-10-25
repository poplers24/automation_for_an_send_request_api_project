from pydantic import  BaseModel, validator

"""schema Company error"""
class Reason(BaseModel):
    reason: str
class CompanyError(BaseModel):
    detail: Reason




# {"detail":{"reason":"Company with requested id: 12 is absent"}}

    """Schema Send request"""
schema_companyList = {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items":
                    {
                        "type": "object",
                        "properties": {
                            "company_id": {
                                "type": "integer"
                            },
                            "company_name": {
                                "type": "string"
                            },
                            "company_address": {
                                "type": "string"
                            },
                            "company_status": {
                                "type": "string",
                                "enum": ["ACTIVE", "CLOSED", "BANKRUPT"]
                            },
                            "description": {
                                "type": "string"
                            },
                            "description_lang": {
                                "type": "array",
                                "items":
                                    {
                                        "type": "object",
                                        "properties": {
                                            "translation_lang": {
                                                "type": "string"
                                            },
                                            "translation": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "translation_lang",
                                            "translation"
                                        ]
                                    }

                            }
                        },
                        "required": [
                            "company_id",
                            "company_name",
                            "company_address",
                            "company_status"
                        ]
                    }

            },
            "meta": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer"
                    },
                    "offset": {
                        "type": "integer"
                    },
                    "total": {
                        "type": "integer"
                    }
                },
                "required": [
                    "total"
                ]
            }
        },
        "required": [
            "data",
            "meta"
        ]
    }
schema_company = {
        "type": "object",
        "properties": {
            "company_id": {
                "type": "integer"
            },
            "company_name": {
                "type": "string"
            },
            "company_address": {
                "type": "string"
            },
            "company_status": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "description_lang": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "translation_lang": {
                            "type": "string"
                        },
                        "translation": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "translation_lang",
                        "translation"
                    ]
                }
            }
        },
        "required": [
            "company_id",
            "company_name",
            "company_address",
            "company_status",
        ]
    }
schema_usersList = {
        "type": "object",
        "properties": {
            "meta": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer"
                    },
                    "offset": {
                        "type": "integer"
                    },
                    "total": {
                        "type": "integer"
                    }
                },
                "required": [
                    "total"
                ]
            },
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": ["string", "null"]
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "company_id": {
                            "type": ["string", "null"]
                        },
                        "user_id": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "last_name",
                        "user_id"
                    ]
                }
            }
        },
        "required": [
            "meta",
            "data"
        ]
    }
schema_responseUser = {
        "type": "object",
        "properties": {
            "first_name": {
                "type": "string"
            },
            "last_name": {
                "type": "string"
            },
            "company_id": {
                "type": "integer"
            },
            "user_id": {
                "type": "integer"
            }
        },
        "required": [
            "last_name",
            "user_id"
        ]
    }
schema_httpValidationError = {
        "type": "object",
        "properties": {
            "detail": {
                "type": "array",
                "items":
                    {
                        "type": "object",
                        "properties": {
                            "loc": {
                                "type": "array",
                                "items": {
                                    "type": [
                                        "string",
                                        "integer"
                                    ]
                                }
                            },
                            "msg": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "loc",
                            "msg",
                            "type"
                        ]
                    }

            }
        },
        "required": [
            "detail"
        ]
    }
schema_meResponse = {
        "type": "object",
        "properties": {
            "token": {
                "type": "string"
            },
            "user_name": {
                "type": "string"
            },
            "email_address": {
                "type": "string",
                "format": "email"
            },
            "valid_till": {
                "type": "string",
                "format": "date-time"
            }
        },
        "required": [
            "token",
            "user_name",
            "email_address",
            "valid_till"
        ]
    }
schema_companyError = {
        "type": "object",
        "properties": {
            "detail": {
                "type": "object",
                "properties": {
                    "reason": {
                        "type": "string"
                    }
                },
                "required": [
                    "reason"
                ]
            }
        },
        "required": [
            "detail"
        ]
    }