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

*** Test Cases ***
Valid Status Code For Request Create A Board
    ${resp}                             Create A Board          New Board
    Status Should Be                    200                     ${resp}

Response Should Contain Given Board Name
    [Tags]                                 Validation
    ${board_name}                          Set Variable         New Board
    ${resp}                                Create A Board       ${board_name}
    Request Should Be Successful           ${resp}
    Validate Board Name In The Response    ${resp}      name    ${board_name}

*** Keywords ***
Create Session For Endpoint
    Create Session          trello                    ${TRELLO_URL}

Create A Board
    [Arguments]             ${board_name}
    [Tags]                                            Boards
#    ${board_name}           Set Variable              Board Name
    Set Suite Variable      ${BOARD_NAME}             ${board_name}
    ${resp}                 Post Request              trello      /1/boards/?name=${board_name}&key=${YOUR_KEY}&token=${YOUR_TOKEN}
    Request Should Be Successful                      ${resp}
    Validate Board Name In The Response               ${resp}     name     ${board_name}
    ${board_id}             Take Board Id             ${resp}
    Set Suite Variable      ${BOARD_ID}               ${board_id}

Validate Board Name In The Response
    [Arguments]                         ${resp}         ${key}          ${expected_value}
    ${resp_dict}                        Set Variable    ${resp.json()}
    Dictionary Should Contain Item      ${resp_dict}    ${key}          ${expected_value}

Take Board Id
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${board_id}          Set Variable          ${resp_dict}[id]
    Log                  ${board_id}
    [Return]             ${board_id}