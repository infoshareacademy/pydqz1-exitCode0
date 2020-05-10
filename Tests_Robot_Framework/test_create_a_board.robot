*** Settings ***
Documentation
Library             Collections
Library             RequestsLibrary
Resource            Resources.robot
Suite Setup         Create Session For Endpoint

*** Test Cases ***
Valid Status Code For Request Create A Board
    ${resp}                             Create A Board          New Board
    Status Should Be                    200                     ${resp}

Response Should Contain Given Board Name
    [Tags]                                 Validation
    ${board_name}                          Set Variable         New Board
    ${resp}                                Create A Board       ${board_name}
    Request Should Be Successful           ${resp}
    Validate Response Field                ${resp}      name    ${board_name}

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
    Create Session          trello                    ${TRELLO_URL}

Create A Board
    [Arguments]             ${board_name}
    [Tags]                                            Boards
    ${resp}                 Post Request              trello      /1/boards/?name=${board_name}&key=${YOUR_KEY}&token=${YOUR_TOKEN}
    Request Should Be Successful                      ${resp}
#    Validate Board Name In The Response               ${resp}     name     ${board_name}
    ${board_id}             Take Board Id             ${resp}
    Set Suite Variable      ${BOARD_ID}               ${board_id}
    [Return]                ${resp}

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

Take Board Id
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${board_id}          Set Variable          ${resp_dict}[id]
    Log                  ${board_id}
    [Return]             ${board_id}