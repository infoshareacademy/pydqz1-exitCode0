*** Settings ***
Documentation
Library             Collections
Library             RequestsLibrary
Suite Setup         Create Session For Endpoint

*** Variables ***
${ENDPOINT}            1/boards
${TRELLO_URL}          https://api.trello.com
${YOUR_KEY}            78a2098e65bf7c3f8e585f7ea4c383cf
${YOUR_TOKEN}          23de07f02dac895c62107ae025a18f3e4ee17c18c21d39639ebf2f9bd3a68ed1
${BOARD_ID}            ${board_id}

*** Test Cases ***
Valid Status Code For Request Create A Board
    ${resp}                             Get A Board         ${board_id}
    Status Should Be                    200                 ${resp}

Response Should Contain Given Board Name
    [Tags]                              Validation
    ${resp}                             Get A Board         ${board_id}
    Request Should Be Successful        ${resp}
    Validate Response Field             ${resp}      id     ${board_id}

*** Keywords ***
Create Session For Endpoint
    Create Session      trello               ${TRELLO_URL}

Get A Board
    [Arguments]
    Set Suite Variable     ${BOARD_ID}          ${board_id}
    ${params}           Create Dictionary       id=${board_id}      token=${YOUR_TOKEN}     key=${YOUR_KEY}
    ${resp}             Get Request             trello                       ${ENDPOINT}             params=${params}
    ${resp_json}        To Json                 ${resp.text}                 pretty_print=${True}
    Log                 ${resp_json}
    [Return]            ${resp}

Validate Response Field
    [Arguments]                         ${resp}         ${key}          ${expected_value}
    ${resp_dict}                        Set Variable    ${resp.json()}
    Dictionary Should Contain Item      ${resp_dict}    ${key}          ${expected_value}

