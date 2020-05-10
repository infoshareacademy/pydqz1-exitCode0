*** Settings ***
Documentation
Library             Collections
Library             RequestsLibrary
Suite Setup         Create Session For Endpoint
Resource            Resources.robot

*** Test Cases ***
Valid Status Code For Request Create A Board
    ${resp}                             Create A Board         New Board
    Status Should Be                    200                    ${resp}

Response Should Contain Given Board Name
    [Tags]                              Validation
    ${board_name}                       Set Variable            New Board
    ${resp}                             Create A Board          ${board_name}
    Request Should Be Successful        ${resp}
    Validate Response Field             ${resp}     name        ${board_name}

*** Keywords ***
Create Session For Endpoint
    Create Session      trello               ${TRELLO_URL}

Create A Board
    [Arguments]         ${board_name}
    ${params}           Create Dictionary       name=${board_name}  token=${YOUR_TOKEN}     key=${YOUR_KEY}
    ${resp}             Post Request            trello              ${ENDPOINT}             params=${params}
    ${resp_json}        To Json                 ${resp.text}        pretty_print=${True}
    Log                 ${resp_json}
    [Return]            ${resp}

Validate Response Field
    [Documentation]
    [Arguments]                         ${resp}         ${key}          ${expected_value}
    ${resp_dict}                        Set Variable    ${resp.json()}
    Dictionary Should Contain Item      ${resp_dict}    ${key}          ${expected_value}