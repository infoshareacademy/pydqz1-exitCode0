*** Settings ***
Documentation
Library             Collections
Library             RequestsLibrary
Resource            Resources.robot

Suite Setup         Create Session For Endpoint



*** Test Cases ***
Valid Status Code For Request Create A Board
    ${resp}                             Get A Board         ${BOARD_ID}
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
    [Arguments]            ${board_id}
    Set Suite Variable     ${BOARD_ID}          ${board_id}
    ${params}              Create Dictionary       id=${board_id}      token=${YOUR_TOKEN}     key=${YOUR_KEY}
    ${resp}                Get Request             trello                       ${ENDPOINT}             params=${params}
    ${resp_json}           To Json                 ${resp.text}                 pretty_print=${True}
    Log                    ${resp.text}
    [Return]               ${resp}

Validate Response Field
    [Arguments]                         ${resp}         ${key}          ${expected_value}
    ${resp_dict}                        Set Variable    ${resp.json()}
    Dictionary Should Contain Item      ${resp_dict}    ${key}          ${expected_value}

