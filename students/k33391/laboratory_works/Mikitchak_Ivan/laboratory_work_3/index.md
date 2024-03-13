# Лабораторная работа 3

## SameAgentsLegalPersons
__URL__: /app/same-agents-lps/30/

__Usage examples__
Request
__GET__: 
```
{
}
```
Response
```
[
    {
        "id": 45,
        "full_name": "Brown and Sons",
        "short_name": "Brown and Sons",
        "address": "1695 Brendan Gardens\nLake Miguelberg, AL 06203",
        "bank_credentials": "6517946677",
        "specialization": 10
    },
    {
        "id": 62,
        "full_name": "Martinez, Stokes and Leblanc",
        "short_name": "Martinez, Stokes and Leblanc",
        "address": "Unit 1596 Box 3862\nDPO AA 15070",
        "bank_credentials": "7190613049",
        "specialization": 11
    },
    {
        "id": 92,
        "full_name": "Rodriguez Ltd",
        "short_name": "Rodriguez Ltd",
        "address": "54902 Steven Prairie\nJenniferhaven, CT 33616",
        "bank_credentials": "2742518368",
        "specialization": 3
    }
]
```

## AgentContractsStats
__URL__: /app/agent-contracts-stats/30/

__Usage examples__
Request
__GET__: 
```
{
    "since": "2021-01-01",
    "till": "2023-01-01"
}
```
Response
```
{"natural_person_contracts_count":10,"legal_person_contracts_count":1}
```

## InsuredColleagues
__URL__: /app/insured-colleagues/50/

__Usage examples__
Request
__GET__: 
```
{
}
```
Response
```
[
    {
        "id": 5081,
        "full_name": "Steven Mcdaniel",
        "age": 23,
        "risk_category": "L",
        "contract": 8
    },
    {
        "id": 5082,
        "full_name": "Miranda Long",
        "age": 38,
        "risk_category": "L",
        "contract": 8
    },
    {
        "id": 5083,
        "full_name": "Tracy Baker",
        "age": 33,
        "risk_category": "H",
        "contract": 8
    },
    {
        "id": 5084,
        "full_name": "Kristen Thornton",
        "age": 39,
        "risk_category": "H",
        "contract": 8
    },
    {
        "id": 5085,
        "full_name": "Joseph Johnson",
        "age": 25,
        "risk_category": "H",
        "contract": 8
    },
    ...
]
```

## InsuredEventsTimeframe
__URL__: /app/insured-events-timeframe/

__Usage examples__
Request
__GET__: 
```
{
    "since": "2021-01-01",
    "till": "2023-01-01"
}
```
Response
```
{"natural_contracts_payments":328233572,"legal_contracts_payments":19030126}
```
## LegalPersonsAndContracts
__URL__: /app/lps-and-contracts/

__Usage examples__
Request
__GET__: 
```
{
}
```
Response
```
[
    {
        "id": 1,
        "full_name": "Hurst Group",
        "contracts": [
            {
                "id": 1,
                "since": "2021-09-07",
                "till": "2022-04-14",
                "low_premium": 1378,
                "medium_premium": 3690,
                "high_premium": 4130,
                "low_payment": 89570,
                "medium_payment": 239850,
                "high_payment": 268450,
                "agent": 7,
                "legal_person": 1
            }
        ]
    },
    {
        "id": 2,
        "full_name": "Price PLC",
        "contracts": [
            {
                "id": 2,
                "since": "2023-09-16",
                "till": "2027-01-12",
                "low_premium": 1040,
                "medium_premium": 2574,
                "high_premium": 6940,
                "low_payment": 86320,
                "medium_payment": 213642,
                "high_payment": 576020,
                "agent": 45,
                "legal_person": 2
            }
        ]
    },
    {
        "id": 3,
        "full_name": "Ingram, Adams and Duran",
        "contracts": [
            {
                "id": 3,
                "since": "2019-05-03",
                "till": "2021-10-30",
                "low_premium": 1327,
                "medium_premium": 2331,
                "high_premium": 6311,
                "low_payment": 87582,
                "medium_payment": 153846,
                "high_payment": 416526,
                "agent": 25,
                "legal_person": 3
            }
        ]
    },
    {
        "id": 4,
        "full_name": "Combs, Ramos and Bowman",
        "contracts": [
            {
                "id": 4,
                "since": "2022-09-16",
                "till": "2024-06-30",
                "low_premium": 1714,
                "medium_premium": 2967,
                "high_premium": 5723,
                "low_payment": 133692,
                "medium_payment": 231426,
                "high_payment": 446394,
                "agent": 43,
                "legal_person": 4
            }
        ]
    },
    {
        "id": 5,
        "full_name": "Lucero, Miller and Short",
        "contracts": [
            {
                "id": 5,
                "since": "2022-06-29",
                "till": "2022-12-10",
                "low_premium": 1344,
                "medium_premium": 3148,
                "high_premium": 5305,
                "low_payment": 76608,
                "medium_payment": 179436,
                "high_payment": 302385,
                "agent": 22,
                "legal_person": 5
            }
        ]
    },
    ...
]
```
## Report
__Usage examples__
__Method__: GET
__URL__: /app/report/
Request
```
{
}
```
Response
```
[
    {
        "id": 3,
        "full_name": "Nathan White",
        "natural_contracts_count": 15,
        "natural_contracts_premium": 43075,
        "natural_contracts_payment": 2558260,
        "legal_contracts_count": 1,
        "legal_contracts_low_premium": 1076,
        "legal_contracts_medium_premium": 2939,
        "legal_contracts_high_premium": 7166,
        "legal_contracts_low_payment": 11836,
        "legal_contracts_medium_payment": 32329,
        "legal_contracts_high_payment": 78826
    },
    {
        "id": 4,
        "full_name": "Christopher Gray",
        "natural_contracts_count": 14,
        "natural_contracts_premium": 42012,
        "natural_contracts_payment": 2168898,
        "legal_contracts_count": 2,
        "legal_contracts_low_premium": 3096,
        "legal_contracts_medium_premium": 6002,
        "legal_contracts_high_premium": 11915,
        "legal_contracts_low_payment": 129988,
        "legal_contracts_medium_payment": 306336,
        "legal_contracts_high_payment": 531906
    },
    {
        "id": 5,
        "full_name": "Shannon Vance",
        "natural_contracts_count": 15,
        "natural_contracts_premium": 46153,
        "natural_contracts_payment": 3023450,
        "legal_contracts_count": 1,
        "legal_contracts_low_premium": 1192,
        "legal_contracts_medium_premium": 3440,
        "legal_contracts_high_premium": 5897,
        "legal_contracts_low_payment": 51256,
        "legal_contracts_medium_payment": 147920,
        "legal_contracts_high_payment": 253571
    },
    ...
]
```

## Agent
__Usage examples__
__Method__: GET
__URL__: /app/agents/
Request:
```
{
}
```
Response:
```
[
    {
        "id": 3,
        "full_name": "Nathan White",
        "passport_data": "5583547680",
        "contact_data": "918-722-0870x02561"
    },
    {
        "id": 4,
        "full_name": "Christopher Gray",
        "passport_data": "8860828429",
        "contact_data": "669.506.6057x48229"
    },
    {
        "id": 5,
        "full_name": "Shannon Vance",
        "passport_data": "3685439006",
        "contact_data": "313-881-3874x566"
    },
    {
        "id": 6,
        "full_name": "Shelley Kramer",
        "passport_data": "7004725705",
        "contact_data": "(371)696-3456x540"
    },
    ...
]
```
__Method__: POST
__URL__: /app/agents/
Request:
```
{
    "full_name": "Jimmy McGill",
    "passport_data": "7224725607",
    "contact_data": "(371)555-35-35"
}
```
Response:
```
{
    "id": 53,
    "full_name": "Jimmy McGill",
    "passport_data": "7224725607",
    "contact_data": "(371)555-35-35"
}
```
__Method__: DELETE
__URL__: /app/agents/53/
Request:
```
{
}
```
Response:
```
{
}
```