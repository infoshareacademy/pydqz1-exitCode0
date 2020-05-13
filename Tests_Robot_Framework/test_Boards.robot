*** Settings ***
Documentation       Test for Trello API
Resource            Resources.robot
Library             RequestsLibrary
Library             Collections
Suite Setup         Create Session For Endpoint


*** Test Cases ***
Check If CREATE A BOARD Creates New Board
    [Tags]                                 BOARDS
    ${board_name}                          Set Variable              New Board
    ${resp}                                Create A Board            ${board_name}
    Request Should Be Successful           ${resp}
    Validate Board Name In The Response    ${resp}                   ${board_name}
    ${new_board_id}                        Take ID from New Board    ${resp}
    Set Suite Variable    ${BOARD_ID}      ${new_board_id}

Check If GET A BOARD With Correct Id Returns Expected Board
    [Tags]                                 BOARDS
    ${resp}                                Get A Board         ${BOARD_ID}
    Request Should Be Successful           ${resp}
    Validate Board Id In The Response      ${resp}             ${BOARD_ID}

Check If GET A BOARD With Inorrect Id Returns "Invalid id" In The Response
    [Tags]                                 BOARDS
    ${wrong_board_id}                      Set Variable                  5uu6ta9z1gqgf812yjd6
    ${resp}                                Get A Board With Wrong Id     ${wrong_board_id}
    Validate Bad Status Code        ${resp.status_code}
    Validate "Invalid id" Response  ${resp.content}

Check If NEW LIST Creates List On Selected Board
    [Tags]                                            LISTS
    ${list_name}            Set Variable              New List
    ${resp}                 Create A List             ${list_name}
    Request Should Be Successful                      ${resp}
    ${new_list_id}     Take LIST ID from New List           ${resp}
    Set Suite Variable      ${LIST_ID}                ${new_list_id}


*** Keywords ***
Create Session For Endpoint
    Create Session      trello                 ${URL}

Create A Board
    [Arguments]         ${board_name}
    ${params}           Create Dictionary      name=${board_name}    token=${YOUR_TOKEN}    key=${YOUR_KEY}
    ${resp}             Post Request           trello    ${ENDPOINT}    params=${params}
    ${resp_json}        To Json                ${resp.text}          pretty_print=${True}
    Log                 ${resp_json}
    [Return]            ${resp}

Create A List
    [Arguments]         ${list_name}
    ${params}           Create Dictionary      name=${list_name}    token=${YOUR_TOKEN}    key=${YOUR_KEY}
    ${resp}             Post Request           trello    ${ENDPOINT}/${BOARD_ID}/lists/    params=${params}
    ${resp_json}        To Json                ${resp.text}         pretty_print=${True}
    Log                 ${resp_json}
    [Return]            ${resp}

Get A Board
    [Arguments]         ${BOARD_ID}
    ${params}           Create Dictionary      token=${YOUR_TOKEN}    key=${YOUR_KEY}
    ${resp}             Get Request            trello    ${ENDPOINT1}${BOARD_ID}    params=${params}
    ${resp_json}        To Json                ${resp.text}           pretty_print=${True}
    Log                 ${resp_json}
    [Return]            ${resp}

Get A Board With Wrong Id
    [Arguments]         ${wrong_board_id}
    ${params}           Create Dictionary      token=${YOUR_TOKEN}    key=${YOUR_KEY}
    ${resp}             Get Request            trello    ${ENDPOINT1}${wrong_board_id}    params=${params}
    Log                 ${resp}
    [Return]            ${resp}

Validate Board Name In The Response
    [Arguments]          ${resp}               ${board_name}
    ${resp_dict}         Set Variable          ${resp.json()}
    Should Be Equal As Strings                 ${resp_dict}[name]   ${board_name}

Validate Board Id In The Response
    [Arguments]          ${resp}               ${BOARD_ID}
    ${resp_dict}         Set Variable          ${resp.json()}
    Should Be Equal As Strings                 ${resp_dict}[id]   ${BOARD_ID}

Take ID from New Board
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${board_id}          Set Variable          ${resp_dict}[id]
    Log                  ${board_id}
    [Return]             ${board_id}

Validate Bad Status Code
    [Arguments]         ${resp.status_code}
    Log                 ${resp.status_code}
    ${status}           Convert To String       ${resp.status_code}
    Should Be Equal     ${status}               400

Validate "Invalid id" Response
    [Arguments]         ${resp.content}
    ${response}         Convert To String       ${resp.content}
    Should Be Equal     ${response}             invalid id

Take LIST ID from New List
    [Arguments]          ${resp}
    ${resp_dict}         Set Variable          ${resp.json()}
    ${list_id}           Set Variable          ${resp_dict}[id]
    Log                  ${list_id}
    [Return]             ${list_id}




